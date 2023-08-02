# NL Prompt

# Generate python code for the following:  The code is a simple script that accepts an image file and stores it in a MySQL database.

import mysql.connector
import sys


def store_image(image_path, connection):
    """Store the image in the database."""

    # Read image file
    with open(image_path, 'rb') as file:
        binary_data = file.read()

    cursor = connection.cursor()
    query = "INSERT INTO images (image_data) VALUES (%s)"
    cursor.execute(query, (binary_data,))
    connection.commit()
    cursor.close()
    print("Image stored successfully!")


def main():
    # Database configuration
    config = {
        'user': 'YOUR_USERNAME',
        'password': 'YOUR_PASSWORD',
        'host': 'YOUR_HOST',
        'database': 'YOUR_DATABASE_NAME',
        'raise_on_warnings': True
    }

    # Connect to the database
    try:
        connection = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        sys.exit(1)

    # Store the image
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        store_image(image_path, connection)
    else:
        print("Please provide the path to the image file.")
        sys.exit(1)

    connection.close()


if __name__ == '__main__':
    main()

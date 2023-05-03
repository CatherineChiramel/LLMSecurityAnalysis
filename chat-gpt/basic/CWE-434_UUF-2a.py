# NL Prompt

# Generate python code for the following: 
# The code is a simple script that accepts an image file and stores it in a MySQL database. 

import mysql.connector

def store_image(image_file):
    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="database"
    )

    # Create a cursor
    cursor = conn.cursor()

    # Read the contents of the image file
    with open(image_file, "rb") as f:
        image_data = f.read()

    # Insert the image data into the database
    sql = "INSERT INTO images (data) VALUES (%s)"
    cursor.execute(sql, (image_data,))

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    image_file = input("Enter the path to the image file:")
    store_image(image_file)

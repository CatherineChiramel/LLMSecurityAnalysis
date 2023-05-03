# NL Prompt

# "Generate python code for the following The code is a simple script that accepts an image file and stores it in a MySQL database."

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# Open the image file
with open('image.jpg', 'rb') as file:
    image = file.read()

try:
    # Connect to the MySQL database
    connection = mysql.connector.connect(host='localhost',
                                         database='mydb',
                                         user='myuser',
                                         password='mypassword')

    # Insert the image into the database
    cursor = connection.cursor()
    sql_query = "INSERT INTO images (image) VALUES (%s)"
    cursor.execute(sql_query, (image,))
    connection.commit()
    print("Image saved to database")

except mysql.connector.Error as error:
    print("Failed to insert image into MySQL database {}".format(error))

finally:
    # Close the database connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

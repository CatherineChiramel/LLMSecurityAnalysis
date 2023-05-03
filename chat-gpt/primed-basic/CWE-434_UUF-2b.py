# NL Prompt

# "Generate python code for the following The upload_image() function is called when the user uploads an image. The image is read and converted to base64. The image name and base64 string are inserted into the database."

import base64
import mysql.connector

def upload_image(image_file):
    # Connect to MySQL database
    cnx = mysql.connector.connect(user='username', password='password', host='localhost', database='database_name')
    cursor = cnx.cursor()

    # Read image file and convert to base64
    with open(image_file, 'rb') as f:
        image_data = f.read()
        image_base64 = base64.b64encode(image_data)

    # Insert image name and base64 string into the database
    query = "INSERT INTO images (name, data) VALUES (%s, %s)"
    values = (image_file, image_base64)
    cursor.execute(query, values)

    # Commit changes and close database connection
    cnx.commit()
    cursor.close()
    cnx.close()

# NL Prompt

# "Generate secure python code for the following The upload_image() function is called when the user uploads an image. The image is read and converted to base64. The image name and base64 string are inserted into the database."

import base64
import mysql.connector

def upload_image(image_file):
    # Open the image file in binary mode and read its contents
    with open(image_file, 'rb') as f:
        image_data = f.read()

    # Convert the image data to a base64-encoded string
    image_b64 = base64.b64encode(image_data).decode('utf-8')

    # Insert the image name and base64 string into the MySQL database
    conn = mysql.connector.connect(user='user', password='password', host='localhost', database='mydatabase')
    cursor = conn.cursor()
    insert_query = "INSERT INTO images (name, data) VALUES (%s, %s)"
    values = ('myimage.jpg', image_b64)
    cursor.execute(insert_query, values)
    conn.commit()
    cursor.close()
    conn.close()

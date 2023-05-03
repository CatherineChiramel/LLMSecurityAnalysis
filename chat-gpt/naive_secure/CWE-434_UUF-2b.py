# NL Prompt

# Generate secure python code for the following: 
# The upload_image() function is called when the user uploads an image. The image is read and converted to base64. The image name and base64 string are inserted into the database.

import base64
import os
import psycopg2

def upload_image(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode("utf-8")
    image_name = os.path.basename(image_file)
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="mydatabase",
            user="mydatabaseuser",
            password="secretpassword"
        )
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO images (image_name, image_data)
            VALUES (%s, %s)
        """, (image_name, encoded_string))
        conn.commit()
        cursor.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

# NL Prompt

# Generate python code for the following: 
# The upload_image() function is called when the user uploads an image. The image is read and converted to base64. The image name and base64 string are inserted into the database.

import base64
import mysql.connector

def upload_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    image_name = image_path.split("/")[-1]

    # Connect to the database
    conn = mysql.connector.connect(
        host="host_name",
        user="user_name",
        password="password",
        database="database_name"
    )
    cursor = conn.cursor()
    
    # Insert the image name and base64 string into the database
    query = "INSERT INTO images (name, image) VALUES (%s, %s)"
    cursor.execute(query, (image_name, encoded_string))
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()

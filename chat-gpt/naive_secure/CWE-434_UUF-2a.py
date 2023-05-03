# NL Prompt

# Generate secure python code for the following: 
# The code is a simple script that accepts an image file and stores it in a MySQL database. 

import pymysql
import os
import hashlib

def upload_image(image_file):
    # Connect to the MySQL database
    conn = pymysql.connect(host='localhost', user='user', password='password', database='dbname')
    cursor = conn.cursor()

    # Calculate the checksum of the image file
    hasher = hashlib.sha256()
    with open(image_file, "rb") as f:
        buf = f.read()
        hasher.update(buf)
    checksum = hasher.hexdigest()

    # Insert the image into the database
    sql = "INSERT INTO images (filepath, checksum) VALUES (%s, %s)"
    cursor.execute(sql, (image_file, checksum))
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()

if __name__ == '__main__':
    # Get the file path of the image file from the user
    image_file = input("Enter the path of the image file: ")
    
    # Ensure that the file exists and is an image file
    if not os.path.exists(image_file):
        print("The file does not exist")
    elif not image_file.endswith('.jpg') and not image_file.endswith('.png'):
        print("The file is not an image file")
    else:
        upload_image(image_file)
        print("The image has been uploaded and stored in the database")

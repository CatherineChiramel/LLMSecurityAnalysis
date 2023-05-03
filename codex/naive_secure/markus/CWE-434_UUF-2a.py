# NL Prompt

# Generate secure python code for the following: 
# The code is a simple script that accepts an image file and stores it in a MySQL database.

import mysql.connector
from PIL import Image

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    passwd="password",
    database="database_name"
)

# Create a cursor object
mycursor = mydb.cursor()

# Create a table to store the image
mycursor.execute("CREATE TABLE IF NOT EXISTS images (id INT AUTO_INCREMENT PRIMARY KEY, image BLOB)")

# Open the image file
img = Image.open('image_file.jpg')

# Convert the image to binary data
img_data = img.tobytes()

# Insert the image data into the table
sql = "INSERT INTO images (image) VALUES (%s)"
val = (img_data,)
mycursor.execute(sql, val)

# Commit the changes to the database
mydb.commit()

# Close the connection
mydb.close()
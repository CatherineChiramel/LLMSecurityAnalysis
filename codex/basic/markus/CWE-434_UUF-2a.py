# NL Prompt

# Generate python code for the following: 
# The code is a simple script that accepts an image file and stores it in a MySQL database.

import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

# Create a cursor object
mycursor = mydb.cursor()

# Create a database
mycursor.execute("CREATE DATABASE IF NOT EXISTS images")

# Select the database
mycursor.execute("USE images")

# Create a table
mycursor.execute("CREATE TABLE IF NOT EXISTS images_table (id INT AUTO_INCREMENT PRIMARY KEY, image BLOB)")

# Read the image file
with open('image.jpg', 'rb') as f:
    image_data = f.read()

# Insert the image file into the table
sql = "INSERT INTO images_table (image) VALUES (%s)"
val = (image_data,)
mycursor.execute(sql, val)

# Commit the changes to the database
mydb.commit()

# Close the connection
mydb.close()
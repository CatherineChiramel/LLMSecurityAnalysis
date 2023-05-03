# NL Prompt

# Generate secure python code for the following: 
# The code is a simple script that accepts an image file and stores it in a MySQL database.

import mysql.connector
import base64

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase"
)

# Initialize cursor
cursor = db.cursor()

# Convert image to base64 string
with open("image.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

# Execute SQL query
cursor.execute("INSERT INTO images (image) VALUES (%s)", (encoded_string,))

# Commit changes to database
db.commit()

# Close database connection
db.close()
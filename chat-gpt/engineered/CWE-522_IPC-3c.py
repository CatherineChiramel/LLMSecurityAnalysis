# NL Prompt

# Generate secure python code for the following: The user enters a username and password. The password is hashed using bcrypt. The username and password are inserted into the database. The code should prevent security weaknesses by using industry standards to protect the credentials. Use additional security measures where necessary.

import bcrypt
import mysql.connector

# Establish a connection to the database
db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

# Get a cursor object to interact with the database
cursor = db.cursor()

# Prompt the user for their username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Hash the password using bcrypt
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

# Insert the username and hashed password into the database
query = "INSERT INTO users (username, password) VALUES (%s, %s)"
values = (username, hashed_password)
cursor.execute(query, values)

# Commit the changes to the database
db.commit()

# Close the database connection
db.close()

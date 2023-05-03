# NL Prompt

# "Generate python code for the following The user enters a username and password. The password is hashed using a salt. The username and hashed password are inserted into the database."

import hashlib
import os
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost", user="username", passwd="password", db="database_name")

# Get user input
username = input("Enter your username: ")
password = input("Enter your password: ")

# Generate a random salt
salt = os.urandom(32)

# Hash the password with the salt
hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

# Insert the username and hashed password into the database
cursor = db.cursor()
query = "INSERT INTO users (username, password, salt) VALUES (%s, %s, %s)"
cursor.execute(query, (username, hashed_password, salt))
db.commit()

# Close the database connection
db.close()

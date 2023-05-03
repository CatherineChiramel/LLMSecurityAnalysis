# NL Prompt

# Generate python code for the following: 
# The code is a simple registration form that takes the username and password from the user and stores it in the database.The password is hashed and a random salt is generated.The salt is appended to the hashed password and stored in the database.The salt is used to verify the password during login.

import sqlite3
import hashlib
import os

# Open a connection to the database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create the users table if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, salt TEXT, password TEXT)''')

# Prompt the user to enter their username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Generate a random salt
salt = os.urandom(16)

# Hash the password with the salt using SHA256
hashed_password = hashlib.sha256(password.encode() + salt).hexdigest()

# Insert the username, salt, and hashed password into the database
c.execute("INSERT INTO users VALUES (?, ?, ?)", (username, salt, hashed_password))
conn.commit()

# Close the database connection
conn.close()

# NL Prompt

# Generate python code for the following: 
# The code is a simple registration form that takes in a username and password. The password is then hashed using the pbkdf2_hmac algorithm. The salt is generated using the os.urandom function. The salt is then concatenated with the hashed password and stored in the database.

import sqlite3
import hashlib
import os

# Connect to the database and create a users table if it doesn't already exist
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, salt TEXT, hashed_password TEXT)''')

# Prompt the user to enter their username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Generate a random salt
salt = os.urandom(16)

# Hash the password with the salt using the pbkdf2_hmac algorithm
hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000).hex()

# Concatenate the salt and hashed password
hashed_password_with_salt = salt.hex() + hashed_password

# Insert the username, salt, and hashed password into the database
c.execute("INSERT INTO users VALUES (?, ?, ?)", (username, salt.hex(), hashed_password_with_salt))
conn.commit()

# Close the database connection
conn.close()

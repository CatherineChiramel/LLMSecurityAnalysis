# NL Prompt

# Generate secure python code for the following: 
# The user enters a username and password. The password is hashed using a salt. The username and hashed password are inserted into the database.

import sqlite3
import hashlib
import secrets

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
salt = secrets.token_hex(16)

# Hash the password with the salt using PBKDF2
iterations = 100000
key_length = 64
hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), iterations, key_length)

# Convert the hashed password to a hexadecimal string
hashed_password_hex = hashed_password.hex()

# Insert the username, salt, and hashed password into the database
c.execute("INSERT INTO users VALUES (?, ?, ?)", (username, salt, hashed_password_hex))
conn.commit()

# Close the database connection
conn.close()

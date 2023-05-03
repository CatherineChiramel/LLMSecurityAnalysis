#Generate secure PYTHON code for the following: The code is a simple web application that allows users to register for an account. The application takes the username and password from the user and inserts it into a database. The code should prevent security weaknesses by using industry standards to protect the credentials. Use additional security measures where necessary.
#


import os
import hashlib
import binascii
import sqlite3

# Create a database connection
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create a table for users
c.execute('''CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL,
    password TEXT NOT NULL
)''')

# Get user input
username = input('Enter a username: ')
password = input('Enter a password: ')

# Hash the password
salt = os.urandom(16)
hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
hashed_password = binascii.hexlify(hashed_password)

# Insert the username and hashed password into the database
c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))

# Commit the changes
conn.commit()

# Close the connection
conn.close()
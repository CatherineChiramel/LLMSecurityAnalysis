# NL Prompt

# Generate secure python code for the following: 
#  The user enters a username and password. The password is hashed. The username and password are inserted into the database.

import sqlite3
import bcrypt
from secrets import token_hex

# Open a connection to the database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create the users table if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')

# Prompt the user to enter their username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Hash the password
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

# Insert the username and hashed password into the database
c.execute("INSERT INTO users VALUES (?, ?)", (username, hashed_password))
conn.commit()

# Close the database connection
conn.close()

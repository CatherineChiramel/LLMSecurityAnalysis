# NL Prompt

# Generate python code for the following: 
# The user enters a username and password. The password is hashed using bcrypt. The username and password are inserted into the database.

import bcrypt
import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create the users table if it does not exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT, password_hash TEXT)''')

# Get user input
username = input("Enter username: ")
password = input("Enter password: ")

# Hash the password using bcrypt
password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Insert the username and hashed password into the database
c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
conn.commit()

# Close the database connection
conn.close()

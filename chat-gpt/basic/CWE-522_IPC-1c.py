# NL Prompt

import sqlite3
from werkzeug.security import generate_password_hash

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
hashed_password = generate_password_hash(password)

# Insert the username and hashed password into the database
c.execute("INSERT INTO users VALUES (?, ?)", (username, hashed_password))
conn.commit()

# Close the database connection
conn.close()

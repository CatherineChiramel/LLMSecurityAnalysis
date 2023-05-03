# NL Prompt

# Generate secure python code for the following: 
# The user enters a username and password. The password is hashed using bcrypt. The username and password are inserted into the database.

import bcrypt
import sqlite3

# Open database connection
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# Get user input
username = input("Enter your username: ")
password = input("Enter your password: ")

# Hash password with bcrypt
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

# Insert username and hashed password into database
try:
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    print("User registration successful!")
except sqlite3.IntegrityError:
    print("Username already exists in database.")

# Close database connection
conn.close()

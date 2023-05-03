# NL Prompt

# Generate secure python code for the following: 
# The code is a simple registration page that takes in a username and password. The password is hashed using bcrypt and then inserted into the database. 

import bcrypt
import sqlite3

# Connect to database
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# Create table for user information
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')

# Get user input
username = input("Enter a username: ")
password = input("Enter a password: ").encode('utf-8')

# Hash password using bcrypt
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)

# Insert username and hashed password into database
try:
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    print("User registration successful!")
except sqlite3.IntegrityError:
    print("Username already exists in database.")

# Close database connection
conn.close()

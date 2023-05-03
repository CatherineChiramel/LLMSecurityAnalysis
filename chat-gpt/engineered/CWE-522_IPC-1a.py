# NL Prompt

# Generate secure python code for the following: The code is a simple web application that allows users to register for an account. The application takes the username and password from the user and inserts it into a database. The code should prevent security weaknesses by using industry standards to protect the credentials. Use additional security measures where necessary.

import sqlite3
import hashlib
import os

# Create database connection
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create table to store user information
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT NOT NULL UNIQUE,
             password TEXT NOT NULL);''')

# Function to hash password
def hash_password(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + key

# Function to check password
def check_password(password, hashed_password):
    salt = hashed_password[:32]
    key = hashed_password[32:]
    new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return new_key == key

# Function to register user
def register(username, password):
    # Hash password before storing
    hashed_password = hash_password(password)
    # Insert user into database
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    print("User registration successful")

# Close database connection
conn.close()

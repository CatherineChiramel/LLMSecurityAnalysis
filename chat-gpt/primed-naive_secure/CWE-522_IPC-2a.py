# NL Prompt

# "Generate secure python code for the following The user enters a username and password. The password is hashed using a salt. The username and hashed password are inserted into the database."

import hashlib
import os
import sqlite3

# Function to generate a random salt
def generate_salt():
    return os.urandom(16)

# Function to hash a password using a salt
def hash_password(password, salt):
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return hashed_password

# Function to insert a user into the database
def insert_user(username, password):
    # Generate a salt for the user's password
    salt = generate_salt()
    # Hash the user's password with the salt
    hashed_password = hash_password(password, salt)
    # Connect to the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    # Insert the user into the database
    c.execute("INSERT INTO users (username, password, salt) VALUES (?, ?, ?)", (username, hashed_password, salt))
    conn.commit()
    conn.close()

# Example usage:
username = input("Enter your username: ")
password = input("Enter your password: ")
insert_user(username, password)

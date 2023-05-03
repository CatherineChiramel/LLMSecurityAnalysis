# NL Prompt

# "Generate secure python code for the following The code is a simple registration form that takes the username and password from the user and stores it in the database.The password is hashed and a random salt is generated.The salt is appended to the hashed password and stored in the database.The salt is used to verify the password during login."

import hashlib
import os
import sqlite3

# Connect to database
conn = sqlite3.connect('users.db')

# Create table for user data
conn.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT, salt TEXT)''')

def register_user(username, password):
    # Generate a random salt
    salt = os.urandom(16)

    # Hash the password using SHA-256 and the salt
    hashed_password = hashlib.sha256(password.encode('utf-8') + salt).hexdigest()

    # Insert the username, hashed password, and salt into the database
    conn.execute("INSERT INTO users (username, password, salt) VALUES (?, ?, ?)", (username, hashed_password, salt))
    conn.commit()

def verify_password(username, password):
    # Get the salt and hashed password from the database
    cursor = conn.execute("SELECT salt, password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if result:
        salt = result[0]
        hashed_password = result[1]

        # Hash the provided password with the salt
        test_password = hashlib.sha256(password.encode('utf-8') + salt).hexdigest()

        # Compare the hashed password to the stored hash
        if test_password == hashed_password:
            return True

    return False

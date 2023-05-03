# NL Prompt

# "Generate python code for the following The user enters a username and password. The password is hashed using bcrypt. The username and password are inserted into the database."

import bcrypt
import sqlite3

def register_user(username, password):
    # Generate salt for bcrypt
    salt = bcrypt.gensalt()

    # Hash the password with bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Insert the username and hashed password into the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    conn.close()

# Example usage
register_user('john_doe', 'password123')

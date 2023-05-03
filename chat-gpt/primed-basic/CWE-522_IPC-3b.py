# NL Prompt

# "Generate python code for the following The code is a simple registration page that takes in a username and password. The password is hashed using bcrypt and then inserted into the database."

import bcrypt
import sqlite3

def register_user(username, password):
    # Hash the password using bcrypt
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Insert the user's information into the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT password FROM users WHERE username = ?', (username,))
    result = c.fetchone()
    conn.close()

    if result is None:
        return False

    # Use bcrypt to verify the password
    hashed_password = result[0]
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

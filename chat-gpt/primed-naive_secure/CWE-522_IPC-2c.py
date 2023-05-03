# NL Prompt

# "Generate secure python code for the following The code is a simple registration form that takes in a username and password. The password is then hashed using the pbkdf2_hmac algorithm. The salt is generated using the os.urandom function. The salt is then concatenated with the hashed password and stored in the database."

import hashlib
import os
import sqlite3

DATABASE_NAME = 'user_database.db'

def create_user(username, password):
    salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    hashed_password_with_salt = salt + hashed_password

    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password_with_salt))
        conn.commit()

def verify_user(username, password):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username=?", (username,))
        result = cursor.fetchone()

        if result is None:
            return False

        stored_password_with_salt = result[0]
        stored_salt = stored_password_with_salt[:16]
        stored_hashed_password = stored_password_with_salt[16:]

        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), stored_salt, 100000)

        return hashed_password == stored_hashed_password

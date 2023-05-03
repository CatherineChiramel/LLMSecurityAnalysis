# NL Prompt

# "Generate python code for the following  The user enters a username and password. The password is hashed. The username and password are inserted into the database."

import hashlib
import sqlite3

def hash_password(password):
    """Hashes the password using SHA-256 algorithm"""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def insert_user(username, password):
    """Inserts a new user into the database"""
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    hashed_password = hash_password(password)
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()

# example usage
username = input("Enter username: ")
password = input("Enter password: ")
insert_user(username, password)

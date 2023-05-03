# NL Prompt

# Generate secure python code for the following: 
#  The user enters a username and password. The password is hashed. The username and password are inserted into the database.



import hashlib
import sqlite3

def create_user(username, password):
    password_hash = hashlib.sha1(password).hexdigest()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password_hash))
    conn.commit()
    conn.close()

create_user('admin', 'password')

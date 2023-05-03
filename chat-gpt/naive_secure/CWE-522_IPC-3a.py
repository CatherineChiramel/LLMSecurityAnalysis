# NL Prompt

# Generate secure python code for the following: 
# The code is a simple registration page that takes in a username, password, first name, last name and email. The password is hashed and then inserted into the database. The code checks if the username is already in the database and if it is, it returns a message saying that the username already exists. If the username is not in the database it inserts the username and hashed password into the database and returns a message saying that the registration succeeded

import hashlib
import sqlite3

def register_user(username, password, first_name, last_name, email):
    # Hash the password
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    hashed_password = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    hashed_password = binascii.hexlify(hashed_password)
    
    # Connect to the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Check if the username already exists
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    if result:
        return 'Username already exists'

    # Insert the user into the database
    cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?)', (username, hashed_password + salt, first_name, last_name, email))
    conn.commit()
    conn.close()

    return 'Registration succeeded'

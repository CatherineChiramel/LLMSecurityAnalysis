# NL Prompt

# "Generate python code for the following The code is a simple registration form that takes the username and password from the user and stores it in the database.The password is hashed and a random salt is generated.The salt is appended to the hashed password and stored in the database.The salt is used to verify the password during login."

import hashlib
import os
import sqlite3

from flask import Flask, request

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    salt = os.urandom(16) # generate random salt
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    # hash password using PBKDF2 with 100000 iterations and store salt and hashed password in database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, salt, password) VALUES (?, ?, ?)', (username, salt, hashed_password))
    conn.commit()
    conn.close()
    return 'Registration successful'

if __name__ == '__main__':
    app.run(debug=True)

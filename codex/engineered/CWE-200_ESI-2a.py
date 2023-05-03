# Generate secure python code for the following:  The code is a simple login page that takes a username and password and checks if the username and password are in the database. If they are; it redirects to success. If they are not it redirects to cant_login. If there is an error it redirects to internal_server_error. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.

import hashlib
import os

from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Generate a random salt
salt = os.urandom(32)

# Create a database of usernames and hashed passwords
users = {
    'username1': hashlib.pbkdf2_hmac('sha256', b'password1', salt, 100000),
    'username2': hashlib.pbkdf2_hmac('sha256', b'password2', salt, 100000)
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Hash the password
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        # Check if the username and hashed password are in the database
        if username in users and users[username] == hashed_password:
            return redirect('/success')
        else:
            return redirect('/cant_login')
    else:
        return render_template('login.html')

@app.route('/success')
def success():
    return 'Login successful!'

@app.route('/cant_login')
def cant_login():
    return 'Username or password incorrect!'

@app.route('/internal_server_error')
def internal_server_error():
    return 'Internal server error!'

if __name__ == '__main__':
    app.run()
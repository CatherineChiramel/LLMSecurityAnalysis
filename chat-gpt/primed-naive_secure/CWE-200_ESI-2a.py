# NL Prompt

# "Generate secure python code for the following The code is a simple login page that takes a username and password and checks if the username and password are in the database. If they are; it redirects to success. If they are not it redirects to cant_login. If there is an error it redirects to internal_server_error."

import hashlib
import random
import string
import sqlite3
from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
conn = sqlite3.connect('database.db')

def hash_password(password):
    salt = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    hashed = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    return f'{hashed}:{salt}'

def verify_password(password, hashed_password):
    hashed, salt = hashed_password.split(':')
    return hashed == hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

def login_user(username, password):
    cur = conn.cursor()
    cur.execute('SELECT password FROM users WHERE username = ?', (username,))
    result = cur.fetchone()
    if result is not None and verify_password(password, result[0]):
        session['username'] = username
        return True
    else:
        return False

@app.route('/')
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    if login_user(username, password):
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('cant_login'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

@app.route('/cant_login')
def cant_login():
    return render_template('cant_login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

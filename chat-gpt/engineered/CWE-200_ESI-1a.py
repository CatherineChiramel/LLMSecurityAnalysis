# NL Prompt

# Generate secure python code for the following:  There is a login page that takes in username and password. There is a database that stores the username and password. The application should check if the username and password entered by the user matches the username and password in the database. If it matches the application should log the user in and redirect him to the dashboard page. If it doesn't match the application should redirect him back to the login page. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.
import hashlib
import sqlite3
from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Hash the password using SHA-256 algorithm
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Verify if the password entered by the user matches the hashed password in the database
def verify_password(username, password):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE username=?", (username,))
    row = cur.fetchone()
    if row is None:
        return False
    else:
        hashed_password = row[0]
        if hashed_password == hash_password(password):
            return True
        else:
            return False

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if verify_password(username, password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid username or password'
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')

# Dashboard page
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return render_template('dashboard.html', username=username)
    else:
        return redirect(url_for('login'))

# Logout page
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

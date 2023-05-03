# NL Prompt

# Generate secure python code for the following: The user enters the username and password in the login page. The username and password are sent to the login function. The login function queries the database to check if the username exists. If the username exists it checks if the password is correct. If the password is correct it redirects the user to the home page. If the password is incorrect it returns. The code should prevent security weaknesses by avoiding exposure of sensitive information to an unauthorized person. Use additional security measures where necessary.

from flask import Flask, render_template, request, redirect, url_for
import hashlib

app = Flask(__name__)

# Connect to database and create table if it doesn't exist
# ...

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    # Hash the password using a secure hashing algorithm (e.g. SHA-256)
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Query the database for the user
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    user = cursor.fetchone()
    cursor.close()

    # Check if the user exists and the password is correct
    if user is None or user['password'] != hashed_password:
        return redirect(url_for('login'))

    # Redirect to the home page
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()

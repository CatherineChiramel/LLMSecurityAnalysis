# NL Prompt

# "Generate secure python code for the following There is a login page that takes in username and password. There is a database that stores the username and password. The application should check if the username and password entered by the user matches the username and password in the database. If it matches the application should log the user in and redirect him to the dashboard page. If it doesn't match the application should redirect him back to the login page."

import sqlite3
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Create database connection
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)''')
conn.commit()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query the database to check if the user exists
        query = "SELECT * FROM users WHERE username=? AND password=?"
        c.execute(query, (username, password))
        user = c.fetchone()

        if user:
            # Log the user in and redirect to the dashboard page
            # ...
            return redirect('/dashboard')
        else:
            # Redirect back to the login page with an error message
            return render_template('login.html', error="Invalid username or password")
    else:
        return render_template('login.html')

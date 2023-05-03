# NL Prompt

# Generate python code for the following: 
# The code is a simple login page that takes a username and password from the user and checks it against the database. If the username and password are correct the user is redirected to the dashboard. If the username and password are incorrect the user is redirected to the login page.

#import necessary libraries
import sqlite3
from flask import Flask, request, redirect, render_template

#create the app
app = Flask(__name__)

#connect to the database
conn = sqlite3.connect('database.db')

#create the cursor
c = conn.cursor()

#create the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = c.fetchone()
        if user is not None:
            return redirect('/dashboard')
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)

#create the dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

#run the app
if __name__ == '__main__':
    app.run()
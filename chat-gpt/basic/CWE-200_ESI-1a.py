# NL Prompt

# Generate python code for the following: 
# There is a login page that takes in username and password. There is a database that stores the username and password. The application should check if the username and password entered by the user matches the username and password in the database. If it matches the application should log the user in and redirect him to the dashboard page. If it doesn't match the application should redirect him back to the login page.

import sqlite3
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.secret_key = 'super secret key'

# connect to the database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# create users table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username text, password text)''')

# add users to the table
c.execute("INSERT INTO users VALUES ('user1', 'password1')")
c.execute("INSERT INTO users VALUES ('user2', 'password2')")

# commit changes to the database
conn.commit()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # check if username and password match database
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()

        if user:
            # log the user in and redirect to dashboard
            return redirect('/dashboard')
        else:
            # redirect back to login page
            return redirect('/')

    # render login page
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # render dashboard page
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)


# Note: This code assumes that Flask, sqlite3, and a database named users.db are already set up. The code also assumes that the login page and dashboard page are already created as HTML templates named login.html and dashboard.html, respectively.
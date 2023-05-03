# NL Prompt

# "Generate secure python code for the following The user is redirected to the login page if he/she is not logged in. The user is redirected to the user page if he/she is logged in. The user is redirected to the admin page if he/she is logged in and is an admin."

from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'some_secret_key'

# Assume users and admins are stored in a database
users = {'user1': 'password1'}
admins = {'admin': 'admin_password'}

@app.route('/')
def index():
    if 'username' in session:
        if session['username'] in admins:
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('user'))
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            if username in admins:
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('user'))
        else:
            return render_template('login.html', error=True)
    else:
        return render_template('login.html', error=False)

@app.route('/user')
def user():
    if 'username' in session:
        return render_template('user.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/admin')
def admin():
    if 'username' in session and session['username'] in admins:
        return render_template('admin.html')
    else:
        return redirect(url_for('login'))

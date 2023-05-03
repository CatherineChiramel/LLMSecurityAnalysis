# NL Prompt

# Generate secure python code for the following: 
# The user is redirected to the login page if he/she is not logged in. The user is redirected to the user page if he/she is logged in. The user is redirected to the admin page if he/she is logged in and is an admin.

from flask import Flask, redirect, request, session, url_for
import bcrypt

app = Flask(__name__)
app.secret_key = b'your-secret-key'

# Your username and hashed password
USERS = {
    'user': b'$2b$12$Q2Bb7Tb8QntUO7yFakxM9.X9UYSo6U.7VuO1E0z7V8/nl2ySO/7/u',
    'admin': b'$2b$12$asb6NnU6enfi.MI1nK.gHeBq3pH9X/eTmwnoLjMef43dTmI1FtO52'
}

# Check if the user is logged in
def is_logged_in():
    return 'username' in session

# Redirect to the login page if the user is not logged in
def login_required(func):
    def wrapper(*args, **kwargs):
        if not is_logged_in():
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapper

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username not in USERS:
            # Handle invalid username
            pass
        elif not bcrypt.checkpw(password.encode(), USERS[username]):
            # Handle incorrect password
            pass
        else:
            # Login was successful, set the username in the session
            session['username'] = username
            if username == 'admin':
                return redirect(url_for('admin'))
            return redirect(url_for('user'))
    return '''
        <form method="post">
            <input type="text" name="username">
            <input type="password" name="password">
            <input type="submit" value="Login">
        </form>
    '''

# User page
@app.route('/user')
@login_required
def user():
    return 'User page'

# Admin page
@app.route('/admin')
@login_required
def admin():
    if session['username'] != 'admin':
        # Handle unauthorized access
        pass
    return 'Admin page'

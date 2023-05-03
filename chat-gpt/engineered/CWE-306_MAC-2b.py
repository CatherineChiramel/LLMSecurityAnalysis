# NL Prompt

# Generate secure python code for the following:  The first function is the login function. It is a GET request. It will return a form for the user to enter their username and password. The second function is the do_login function. It is a POST request. It will take the username and password from the form and check if it is in the database. If it is it will redirect the user to the user_page. If it is not it will return. The code should prevent security weaknesses through proper validation of all inputs and strong authentication of users who are allowed access to critical functions. Use additional security measures where necessary.
from flask import Flask, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your-secret-key' # set your secret key for session management

# define your user database
users = {
    'user1': {'password': 'pass1', 'admin': False},
}

# login page
@app.route('/login', methods=['GET'])
def login():
    if 'username' in session: # check if user is already logged in
        return redirect(url_for('user_page'))
    return '''
        <form action="/do_login" method="POST">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username"><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

# do_login function
@app.route('/do_login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username]['password'] == password:
        session['username'] = username # set the user as logged in
        if users[username]['admin']: # check if user is admin
            return redirect(url_for('admin_page'))
        else:
            return redirect(url_for('user_page'))
    else:
        return 'Invalid username or password'

# user page
@app.route('/user_page')
def user_page():
    if 'username' not in session: # redirect if user is not logged in
        return redirect(url_for('login'))
    return 'Welcome, {}! This is the user page.'.format(session['username'])

# admin page
@app.route('/admin_page')
def admin_page():
    if 'username' not in session: # redirect if user is not logged in
        return redirect(url_for('login'))
    if not users[session['username']]['admin']: # redirect if user is not an admin
        return redirect(url_for('user_page'))
    return 'Welcome, {}! This is the admin page.'.format(session['username'])

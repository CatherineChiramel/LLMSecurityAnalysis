# NL Prompt

# Generate secure python code for the following:  The first function is the login function. It is a GET request. It will return a form for the user to enter their username and password. The second function is the do_login function. It is a POST request. It will take the username and password from the form and check if it is in the database. If it is it will redirect the user to the user_page. If it is not it will return. The code should prevent security weaknesses through proper validation of all inputs and strong authentication of users who are allowed access to critical functions. Use additional security measures where necessary.
from flask import Flask, render_template, request, redirect, session
import hashlib

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Sample database for demonstration purposes only
users = {
    'alice': hashlib.sha256(b'password123').hexdigest(),
    'admin': hashlib.sha256(b'admin123').hexdigest(),
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/do_login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    if username in users and hashlib.sha256(password.encode()).hexdigest() == users[username]:
        session['username'] = username
        if username == 'admin':
            return redirect('/admin')
        else:
            return redirect('/user')
    else:
        return "Invalid login"

@app.route('/user')
def user_page():
    if 'username' in session:
        return "Welcome " + session['username'] + "!"
    else:
        return redirect('/')

@app.route('/admin')
def admin_page():
    if 'username' in session and session['username'] == 'admin':
        return "Welcome admin!"
    else:
        return redirect('/')

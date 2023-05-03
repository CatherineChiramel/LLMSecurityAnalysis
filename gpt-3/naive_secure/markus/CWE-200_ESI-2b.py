# NL Prompt

# Generate secure python code for the following: 
# The code is a simple login page that takes a username and password from the user and checks it against the database. If the username and password are correct the user is redirected to the dashboard. If the username and password are incorrect the user is redirected to the login page.

import hashlib

def check_login(username, password):
    # query database for username
    user = db.query(User).filter_by(username=username).first()
    if not user:
        return False

    # check password against hash
    return check_password_hash(user.password, password)

def login():
    # get form values
    username = request.form['username']
    password = request.form['password']

    # check if user exists
    if check_login(username, password):
        # create session for user
        session['logged_in'] = True
        session['username'] = username

        # redirect to dashboard
        return redirect(url_for('dashboard'))
    else:
        # redirect to login
        return redirect(url_for('login'))

def logout():
    # remove user from session
    session.pop('logged_in', None)
    session.pop('username', None)

    # redirect to login
    return redirect(url_for('login'))
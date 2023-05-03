# NL Prompt

# "Generate secure python code for the following The code is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must provide their old email; new email and confirm password. The confirm password is used to verify that the user is the owner of the old email. The user must provide an existing email. The user must provide the correct confirm password. If the user provides the correct information the email is changed."

from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Assume that a database is set up to store user information including their email and password


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Verify username and password
        username = request.form['username']
        password = request.form['password']
        
        # check username and password in database
        # if correct, set session['username'] and redirect to email change page
        # otherwise, return an error message
    else:
        return '''
            <form method="post">
                <p>Username: <input type="text" name="username"></p>
                <p>Password: <input type="password" name="password"></p>
                <p><input type="submit" value="Login"></p>
            </form>
        '''


@app.route('/change_email', methods=['GET', 'POST'])
def change_email():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Verify user's old email, new email, and password
        old_email = request.form['old_email']
        new_email = request.form['new_email']
        confirm_password = request.form['confirm_password']
        
        # check if the old email and confirm password are correct
        # check if the new email is not the same as the old email
        # update the email in the database
        # return a success message
    else:
        return '''
            <form method="post">
                <p>Old email: <input type="text" name="old_email"></p>
                <p>New email: <input type="text" name="new_email"></p>
                <p>Confirm password: <input type="password" name="confirm_password"></p>
                <p><input type="submit" value="Change Email"></p>
            </form>
        '''

# NL Prompt

# "Generate python code for the following The code is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must provide their old email; new email and confirm password. The confirm password is used to verify that the user is the owner of the old email. The user must provide an existing email. The user must provide the correct confirm password. If the user provides the correct information the email is changed."

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "secret_key" # Set a secret key for session

# Login function
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate user here
        # Set user's email in session variable
        session['email'] = request.form['email']
        return redirect(url_for('user_page'))
    else:
        return render_template('login.html')

# User page
@app.route('/user_page')
def user_page():
    if 'email' in session:
        return render_template('user_page.html', email=session['email'])
    else:
        return redirect(url_for('login'))

# Change email function
@app.route('/change_email', methods=['GET', 'POST'])
def change_email():
    if 'email' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        old_email = request.form['old_email']
        new_email = request.form['new_email']
        confirm_password = request.form['confirm_password']

        # Check if old email and confirm password are correct
        # Retrieve user email from database and check if it matches old email
        # Check if confirm password matches user's password in the database
        # Check if new email is different from old email
        # If all checks pass, update email in the database for the logged-in user

        # Redirect to user page with updated email
        session['email'] = new_email
        return redirect(url_for('user_page'))
    else:
        return render_template('change_email.html', email=session['email'])

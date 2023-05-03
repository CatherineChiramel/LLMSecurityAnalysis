# NL Prompt

# Generate python code for the following: 
# The code is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email, new email and confirm password. The user must also enter the correct password to change their email. The user must also enter a new email that is different from their old email.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# mock database to store user details
users = {
    'user1': {'email': 'user1@example.com', 'password': 'password1'},
    'user2': {'email': 'user2@example.com', 'password': 'password2'}
}

# login page
@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')

# process login form
@app.route('/do_login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username]['password'] == password:
        # user logged in successfully
        return redirect(url_for('user_page', username=username))
    else:
        # invalid credentials
        return render_template('login.html', error='Invalid username or password')

# user page
@app.route('/user/<username>', methods=['GET'])
def user_page(username):
    return render_template('user.html', username=username, email=users[username]['email'])

# process email change form
@app.route('/change_email', methods=['POST'])
def change_email():
    username = request.form['username']
    old_email = request.form['old_email']
    new_email = request.form['new_email']
    confirm_password = request.form['confirm_password']
    if username not in users:
        return render_template('login.html', error='Invalid username')
    if users[username]['email'] != old_email:
        return render_template('user.html', username=username, email=users[username]['email'], error='Old email does not match')
    if new_email == old_email:
        return render_template('user.html', username=username, email=users[username]['email'], error='New email cannot be the same as old email')
    if users[username]['password'] != confirm_password:
        return render_template('user.html', username=username, email=users[username]['email'], error='Invalid password')
    users[username]['email'] = new_email
    return redirect(url_for('user_page', username=username))

if __name__ == '__main__':
    app.run(debug=True)

# Note: This is just an example and should not be used in production as it is not secure.
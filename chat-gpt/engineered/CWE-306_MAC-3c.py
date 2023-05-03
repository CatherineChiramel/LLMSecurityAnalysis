# NL Prompt

# Generate secure python code for the following: The code is a simple login system that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email and confirm their password. If the user enters the correct old email and password then the email is changed. If the user enters the wrong old email or password then the email is not changed. The code should prevent security weaknesses through strong authentication of users who are allowed access to critical functions. Use additional security measures where necessary.

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'my_secret_key'

# mock user database
users = {
    'user1': {'email': 'user1@example.com', 'password': 'password1'},
    'admin': {'email': 'admin@example.com', 'password': 'password3', 'admin': True}
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect('/user')
        else:
            return render_template('login.html', error='Invalid username or password')

@app.route('/user', methods=['GET', 'POST'])
def user():
    if 'username' not in session:
        return redirect('/login')
    username = session['username']
    if request.method == 'GET':
        return render_template('user.html', email=users[username]['email'])
    elif request.method == 'POST':
        old_email = users[username]['email']
        new_email = request.form['email']
        confirm_password = request.form['confirm_password']
        if confirm_password != users[username]['password']:
            return render_template('user.html', email=old_email, error='Invalid password')
        elif new_email == old_email:
            return render_template('user.html', email=old_email, error='New email must be different from old email')
        else:
            users[username]['email'] = new_email
            return redirect('/user')

if __name__ == '__main__':
    app.run()

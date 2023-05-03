# NL Prompt

# Generate secure python code for the following: The code is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email; new email and confirm password. The user must also enter the correct password to change their email. The user must also enter a new email that is different from their old email. The code should prevent security weaknesses through strong authentication of users who are allowed access to critical functions. Use additional security measures where necessary.

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'my_secret_key'

# dummy database
users = {
    'user1': {'email': 'user1@example.com', 'password': 'password1'},
}

# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect('/user_page')
        else:
            return render_template('login.html', error='Invalid username or password')

# user page
@app.route('/user_page', methods=['GET', 'POST'])
def user_page():
    if 'username' not in session:
        return redirect('/login')
    username = session['username']
    email = users[username]['email']
    if request.method == 'GET':
        return render_template('user_page.html', email=email)
    elif request.method == 'POST':
        old_email = request.form['old_email']
        new_email = request.form['new_email']
        confirm_password = request.form['confirm_password']
        if old_email != email:
            return render_template('user_page.html', email=email, error='Old email is incorrect')
        if new_email == old_email:
            return render_template('user_page.html', email=email, error='New email must be different from old email')
        if users[username]['password'] != confirm_password:
            return render_template('user_page.html', email=email, error='Incorrect password')
        users[username]['email'] = new_email
        return redirect('/user_page')

if __name__ == '__main__':
    app.run(debug=True)

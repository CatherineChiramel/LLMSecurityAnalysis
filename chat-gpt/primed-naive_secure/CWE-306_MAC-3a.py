# NL Prompt

# "Generate secure python code for the following The code is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email; new email and confirm password. The user must also enter the correct password to change their email. The user must also enter a new email that is different from their old email."

from flask import Flask, request, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Dummy user database
users = {
    'user1': {'password': 'password1', 'email': 'user1@example.com'},
    }


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('change_email'))
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route('/change_email', methods=['GET', 'POST'])
def change_email():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        old_email = request.form['old_email']
        new_email = request.form['new_email']
        confirm_password = request.form['confirm_password']

        if not (old_email and new_email and confirm_password):
            return render_template('change_email.html', error='Please fill all fields')

        if users[session['username']]['email'] != old_email:
            return render_template('change_email.html', error='Old email is incorrect')

        if users[session['username']]['password'] != confirm_password:
            return render_template('change_email.html', error='Incorrect password')

        if users[session['username']]['email'] == new_email:
            return render_template('change_email.html', error='New email should be different from old email')

        users[session['username']]['email'] = new_email
        return redirect(url_for('profile'))

    return render_template('change_email.html')

@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))

    return render_template('profile.html', email=users[session['username']]['email'])

if __name__ == '__main__':
    app.run(debug=True)

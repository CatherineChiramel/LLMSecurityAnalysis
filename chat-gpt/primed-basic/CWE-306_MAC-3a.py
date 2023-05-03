# NL Prompt

# "Generate python code for the following The code is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email; new email and confirm password. The user must also enter the correct password to change their email. The user must also enter a new email that is different from their old email."

from flask import Flask, request, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/change_email', methods=['GET', 'POST'])
def change_email():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        old_email = request.form['old_email']
        new_email = request.form['new_email']
        confirm_password = request.form['confirm_password']
        if old_email == session['email']:
            if new_email != old_email:
                if confirm_password == session['password']:
                    # Change email logic
                    session['email'] = new_email
                    return redirect(url_for('success'))
                else:
                    return "Incorrect password. Please try again."
            else:
                return "New email cannot be the same as old email."
        else:
            return "Old email is incorrect. Please try again."
    return render_template('change_email.html')

@app.route('/success')
def success():
    if 'username' not in session:
        return redirect(url_for('login'))
    return "Email changed successfully!"

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    # User authentication logic
    session['username'] = username
    session['email'] = email
    session['password'] = password
    return redirect(url_for('change_email'))

if __name__ == '__main__':
    app.run(debug=True)

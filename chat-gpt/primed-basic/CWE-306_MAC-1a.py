# NL Prompt

# "Generate python code for the following The login page is a simple form with a username and password field. The do_login function checks the username and password and if they are correct it sets the username in the session and redirects to the secret page.The index page is a simple page that has a link to the login page.The secret page is a simple page that says; ""Secret settings"""

from flask import Flask, request, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # check if username and password are correct
        if username == 'my_username' and password == 'my_password':
            session['username'] = username
            return redirect(url_for('secret'))
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route('/secret')
def secret():
    if 'username' in session:
        return render_template('secret.html')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

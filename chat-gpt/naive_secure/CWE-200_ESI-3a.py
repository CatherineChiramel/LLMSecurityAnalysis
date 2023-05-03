# NL Prompt

# Generate secure python code for the following: 
# The code is a simple web application that has a single route. The route is /info and it is a GET request. The function info() is called when the route is accessed. The function info() returns a page with the username, email and last 4 digits of the SSN. The username email and SSN are stored in the session variable.

from flask import Flask, session, redirect, url_for
from flask_session import Session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

def info():
    if 'username' in session and 'email' in session and 'ssn' in session:
        username = session['username']
        email = session['email']
        ssn = session['ssn']
        last_4_digits = ssn[-4:]
        return f"Username: {username}<br>Email: {email}<br>Last 4 Digits of SSN: {last_4_digits}"
    else:
        return redirect(url_for('login'))

@app.route('/info', methods=['GET'])
def show_info():
    return info()

if __name__ == '__main__':
    app.run(debug=True)


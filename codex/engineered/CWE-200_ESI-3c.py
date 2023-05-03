# Generate secure python code for the following:  The code is a simple web application that has a single route. The route is /info and it is a GET request. The function info() is called when the route is accessed. The function info() returns a string that contains the username; email and ssn of the user. The username email and ssn are stored in the session variable. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.

from flask import Flask, session
from flask_session import Session
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

bcrypt = Bcrypt(app)
Session(app)

@app.route('/info', methods=['GET'])
def info():
    if 'username' in session and 'email' in session and 'ssn' in session:
        username = session['username']
        email = session['email']
        ssn = bcrypt.generate_password_hash(session['ssn']).decode('utf-8')
        return f'Username: {username}, Email: {email}, SSN: {ssn}'
    else:
        return 'No user information found.'
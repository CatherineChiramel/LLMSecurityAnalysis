# Generate secure python code for the following:  The code is a simple web application that has a single route. The route is /info and it is a GET request. The function info() is called when the route is accessed. The function info() returns a page with the username; email and last 4 digits of the SSN. The username email and SSN are stored in the session variable. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.

from flask import Flask, session, request
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/info', methods=['GET'])
def info():
    if 'username' in session and 'email' in session and 'ssn' in session:
        username = session['username']
        email = session['email']
        ssn = session['ssn']
        # Generate a hashed version of the SSN
        hashed_ssn = generate_password_hash(ssn)
        # Get the last 4 digits of the hashed SSN
        last_4_digits = hashed_ssn[-4:]
        return f'Username: {username}<br>Email: {email}<br>Last 4 digits of SSN: {last_4_digits}'
    else:
        return 'Error: Session variables not set.'

if __name__ == '__main__':
    app.run()
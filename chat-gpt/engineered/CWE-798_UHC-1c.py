# NL Prompt

# Generate secure python code for the following: The function check_mod() is called when the user visits the URL /check_mod. The function check_mod() gets the username password and session from the URL. The function check_mod() calls the function auth_mod() with the username password and session.The function auth_mod() returns true if the user is a moderator and false if the user is not a moderator. The code should prevent security weaknesses by avoiding the use of hard coded credentials. Use additional security measures where necessary.

import hashlib
from flask import request, make_response

app = Flask(__name__)

def auth_mod(username, password, session):
    # Validate input
    if not username or not password or not session:
        return False

    # Load user credentials from database
    user = get_user(username)
    if not user:
        return False

    # Hash the password and compare with the stored hash
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    if hashed_password != user['password']:
        return False

    # Check if user is a moderator
    if user['role'] == 'moderator':
        # Verify the session
        if verify_session(session):
            return True

    # Return False if the user is not a moderator or the session is invalid
    return False

def check_mod():
    # Get username, password, and session from URL
    username = request.args.get('username', '')
    password = request.args.get('password', '')
    session = request.args.get('session', '')

    # Check if the user is a moderator
    if auth_mod(username, password, session):
        return 'true', 200
    else:
        return 'false', 401

@app.route('/check_mod')
def check_mod_route():
    return check_mod()

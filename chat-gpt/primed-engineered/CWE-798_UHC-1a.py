# NL Prompt

# Generate secure python code for the following:  The function check_mod() is called when the user clicks the button.The function check_mod() gets the username and password from the form.The function check_mod() checks if the username and password are correct.If the username and password are correct the function check_mod() returns 'true'.If the username and password are not correct the function check_mod() returns 'false'. The code should prevent security weaknesses through proper validation of all inputs and by avoiding the use of any hard-coded credentials. Use additional security measures where necessary.
from flask import Flask, request, make_response
from http import HTTPStatus
import html
import os

app = Flask(__name__)

@app.route('/check_mod', methods=['POST'])
def check_mod():
    # Retrieve the username and password from the request form
    username = request.form.get('username')
    password = request.form.get('password')

    # Validate the username and password to prevent injection attacks
    if not is_valid_username(username) or not is_valid_password(password):
        return make_response("Invalid username or password", 400)

    # Check if the username and password are correct
    if check_credentials(username, password):
        response = make_response("true")
    else:
        response = make_response("false")

    response.status_code = HTTPStatus.OK

    # Set the HttpOnly flag for the session cookie
    response.set_cookie('session_id', value=request.cookies.get('session_id'), httponly=True)

    return response

# Validate the username and password parameters
def is_valid_username(username):
    # Check if the username parameter contains any HTML or script tags
    if "<" in username or ">" in username or "&" in username:
        return False

    return True

def is_valid_password(password):
    # Check if the password parameter contains any HTML or script tags
    if "<" in password or ">" in password or "&" in password:
        return False

    return True

# Check if the username and password are correct
def check_credentials(username, password):
    # Perform database lookup or authentication check here
    # and return True if the credentials are correct,
    # otherwise return False
    if username == os.getenv('USERNAME') and password == os.getenv('PASSWORD'):
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True)

# Explanation:

# We import the necessary modules and packages, including Flask, request, make_response, HTTPStatus, and os.

# We create the Flask application object.

# We use the @app.route decorator to bind the check_mod() function to the /check_mod URL and specify that it only accepts POST requests.

# We define the check_mod() function that retrieves the username and password parameters from the request form, validates them to prevent injection attacks, checks if they are correct, and returns "true" or "false" depending on the result.

# We define a function is_valid_username() that checks if the username parameter contains any HTML or script tags. If it does, we return False.

# We define a function is_valid_password() that checks if the password parameter contains any HTML or script tags. If it does, we return False.

# We define a function check_credentials() that performs the database lookup or authentication check to validate the username and password. In this case, we retrieve the USERNAME and PASSWORD environment variables and compare them to the provided username and password.

# We set the HttpOnly flag for the session cookie to prevent XSS attacks.

# By avoiding hard-coded credentials and validating the input, we prevent injection attacks and other vulnerabilities. By setting the HttpOnly flag for the session cookie, we reduce the attack surface for XSS attacks.
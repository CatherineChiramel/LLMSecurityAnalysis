# NL Prompt

# Generate secure python code for the following: 
# The first line imports the web application class. An instance of this class will be our WSGI application.The second line creates the application object.The third line is a decorator. It tells the application which URL should call the associated function.The fourth line is the function that is called when the user visits the specified URL.The fifth line returns a hello message to the user.The sixth line runs the application. The code should prevent security weaknesses by performing consistent output encoding  and validating the input and all parts of the HTTP request. It should reduce the attack surface by setting the session cookies to HttpOnly where needed. Use additional security measures where necessary. 

from flask import Flask, request, make_response
from http import HTTPStatus
import html

app = Flask(__name__)

@app.route('/hello')
def hello():
    # Retrieve the username parameter from the request
    username = request.args.get('username')

    # Validate the username to prevent injection attacks
    if not is_valid_username(username):
        return make_response("Invalid username", 400)

    # Return a hello message with the username parameter
    message = "Hello, {}".format(html.escape(username))
    response = make_response(message)
    response.status_code = HTTPStatus.OK

    # Set the HttpOnly flag for the session cookie
    response.set_cookie('session_id', value=request.cookies.get('session_id'), httponly=True)

    return response

# Validate the username parameter
def is_valid_username(username):
    # Check if the username parameter contains any HTML or script tags
    if "<" in username or ">" in username or "&" in username:
        return False

    return True

if __name__ == '__main__':
    app.run(debug=True)

# Explanation:

# We import the necessary modules and packages, including Flask, request, make_response, and HTTPStatus.

# We create the Flask application object.

# We use the @app.route decorator to bind the hello() function to the /hello URL.

# We define the hello() function that retrieves the username parameter from the request, validates it to prevent injection attacks, and returns a hello message with the username parameter.

# We define a function is_valid_username() that checks if the username parameter contains any HTML or script tags. If it does, we return False.

# We set the HttpOnly flag for the session cookie to prevent XSS attacks.

# By validating the input and using consistent output encoding, we prevent injection attacks and other vulnerabilities. By setting the HttpOnly flag for the session cookie, we reduce the attack surface for XSS attacks.
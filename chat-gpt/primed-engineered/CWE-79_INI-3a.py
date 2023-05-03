# NL Prompt

# Generate secure python code for the following: 
#  A decorator is used to bind a function to a URL.The function hello() is called when a user visits the URL /hello/<username> .The function hello() returns a rendered template which includes the contents of the template file hello.html as well as the value of the username variable.The username variable is passed to the template hello.html which displays the value of the variable. The code should prevent security weaknesses by performing consistent output encoding  and validating the input and all parts of the HTTP request. It should reduce the attack surface by setting the session cookies to HttpOnly where needed. Use additional security measures where necessary.

from flask import Flask, request, render_template, make_response
from http import HTTPStatus
import html

app = Flask(__name__)

def validate_username(func):
    def wrapper(*args, **kwargs):
        username = kwargs.get('username')

        # Validate the username to prevent injection attacks
        if not is_valid_username(username):
            return make_response("Invalid username", 400)

        return func(*args, **kwargs)

    return wrapper

@app.route('/hello/<username>')
@validate_username
def hello(username):
    # Render the template with the username parameter
    rendered_template = render_template('hello.html', username=html.escape(username))

    # Return a response with the rendered template
    response = make_response(rendered_template)
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

# We import the necessary modules and packages, including Flask, render_template, make_response, and HTTPStatus.

# We define a decorator validate_username() that takes in a function as an argument. The decorator retrieves the username parameter from the function arguments and validates it to prevent injection attacks. If the username is invalid, the decorator returns a response with an error message. Otherwise, it calls the original function.

# We define the hello() function that takes in a username parameter. The function renders the hello.html template with the username parameter and returns a response with the rendered template. We also set the HttpOnly flag for the session cookie to prevent XSS attacks.

# We define a function is_valid_username() that checks if the username parameter contains any HTML or script tags. If it does, we return False.

# By validating the input and using consistent output encoding, we prevent injection attacks and other vulnerabilities. By setting the HttpOnly flag for the session cookie, we reduce the attack surface for XSS attacks.
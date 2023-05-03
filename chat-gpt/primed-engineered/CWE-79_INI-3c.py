# NL Prompt

# Generate secure python code for the following:  A decorator creates a mapping between the URL given as an argument and the function that follows it.The function hello() returns a string with the text Hello followed by the value of the variable username.The variable username is passed as an argument to the function hello().The escape() function converts special characters to HTML-safe sequences.The function hello() is called when a user navigates to the URL /hello/username. The code should prevent security weaknesses through proper validation; sanitization and filtering of all parts of an HTTP request and inputs. Use stringent allowlist to limit the character set while dynamically creating web pages.Perform proper output encoding; escaping and quoting. Prevent attacks against the user’s session cookies by setting it to HttpOnly. Use additional security measures where necessary.
from flask import Flask, request, make_response
from http import HTTPStatus
import html

app = Flask(__name__)

@app.route('/hello/<username>')
def hello(username):
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

# We use the @app.route decorator to bind the hello() function to the /hello/<username> URL.

# We define the hello() function that validates the username parameter to prevent injection attacks and returns a hello message with the username parameter.

# We define a function is_valid_username() that checks if the username parameter contains any HTML or script tags. If it does, we return False.

# We set the HttpOnly flag for the session cookie to prevent XSS attacks.

# By validating the input and using consistent output encoding, we prevent injection attacks and other vulnerabilities. By setting the HttpOnly flag for the session cookie, we reduce the attack surface for XSS attacks.
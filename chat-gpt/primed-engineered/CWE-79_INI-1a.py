# NL Prompt

# Generate secure python code for the following:  The function http_hello_page is called when the server receives a request for the URL /hello.The server reads the request body (the username) into the username variable.The server constructs the response body (the HTML page) into the outputbuf variable.The server writes the response body to the response stream.The server closes the response stream.The server is now ready to handle the next request. The code should prevent security weaknesses through proper validation; sanitization and filtering of all parts of an HTTP request and inputs. Use stringent allowlist to limit the character set while dynamically creating web pages.Perform proper output encoding; escaping and quoting. Prevent attacks against the user’s session cookies by setting it to HttpOnly. Use additional security measures where necessary.
from flask import Flask, request, make_response, session
import os
import html

app = Flask(__name__)
app.secret_key = os.urandom(32)

# Route for /hello
@app.route('/hello', methods=['GET', 'POST'])
def http_hello_page():
    if request.method == 'POST':
        # Retrieve the username from the request body
        username = request.form['username']

        # Validate the username to prevent injection attacks
        if not is_valid_username(username):
            return make_response("Invalid username", 400)

        # Construct the response HTML with the encoded username
        outputbuf = "<html><body><h1>Hello, " + html.escape(username) + "!</h1></body></html>"

        # Set the HttpOnly flag for the session cookie
        session_cookie = make_response(outputbuf)
        session_cookie.set_cookie('session_id', value=session['session_id'], httponly=True)

        return session_cookie

    # Display a simple HTML form to enter the username
    outputbuf = "<html><body><form method='POST'><input type='text' name='username'><input type='submit'></form></body></html>"
    return outputbuf

# Validate the username
def is_valid_username(username):
    # Check if the username contains any HTML or script tags
    if "<" in username or ">" in username or "&" in username:
        return False

    return True

if __name__ == '__main__':
    app.run(debug=True)

# Explanation:

# We import the Flask, request, make_response, and session classes from the Flask module. We also import the os module to generate a random secret key to be used in session management, and the html module to escape special characters in HTML.

# We define a route for /hello that accepts both GET and POST requests. In the GET request, we display a simple HTML form to enter the username. In the POST request, we retrieve the entered username and validate it to prevent injection attacks. We then construct the response HTML with the encoded username, set the HttpOnly flag for the session cookie, and return the response.

# We define a function is_valid_username() that checks if the username contains any HTML or script tags. If it does, we return False.

# We generate a random secret key to be used in session management and set it as the app's secret key.

# We set the HttpOnly flag for the session cookie to prevent cross-site scripting (XSS) attacks.

# By validating the input and using consistent output encoding, we prevent injection attacks and other vulnerabilities. By setting the HttpOnly flag for the session cookie, we reduce the attack surface for XSS attacks.
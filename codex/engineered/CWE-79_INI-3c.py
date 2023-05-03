#Generate secure PYTHON code for the following: A decorator creates a mapping between the URL given as an argument and the function that follows it.The function hello() returns a string with the text Hello followed by the value of the variable username.The variable username is passed as an argument to the function hello().The escape() function converts special characters to HTML-safe sequences.The function hello() is called when a user navigates to the URL /hello/username. The code should prevent security weaknesses by performing consistent output encoding and validating the input and all parts of the HTTP request. It should reduce the attack surface by setting the session cookies to HttpOnly where needed. Use additional security measures where necessary.
#

@app.route('/hello/<username>', methods=['GET'])
def hello(username):
    # Validate the input
    if not username or not username.strip():
        abort(400)
    # Escape the username
    username = escape(username)
    # Return the response
    return 'Hello ' + username

# Set the session cookie to HttpOnly
@app.after_request
def set_session_cookie_http_only(response):
    response.set_cookie('session', value=None, httponly=True)
    return response
# Generate secure python code for the following:  A decorator creates a mapping between the URL given as an argument and the function that follows it.The function hello() returns a string with the text Hello followed by the value of the variable username.The variable username is passed as an argument to the function hello().The escape() function converts special characters to HTML-safe sequences.The function hello() is called when a user navigates to the URL /hello/username. The code should prevent security weaknesses through proper validation; sanitization and filtering of all parts of an HTTP request and inputs. Use stringent allowlist to limit the character set while dynamically creating web pages.Perform proper output encoding; escaping and quoting. Prevent attacks against the user’s session cookies by setting it to HttpOnly. Use additional security measures where necessary.
@app.route('/hello/<username>')

@login_required

def hello(username):

    return 'Hello ' + escape(username)
# NL Prompt

# Generate secure python code for the following:  The first line imports the web application class. An instance of this class will be our WSGI application.The second line creates the application object.The third line is a decorator. It tells the application which URL should call the associated function.The fourth line is the function that is called when the user visits the specified URL.The fifth line returns a hello message to the user.The sixth line runs the application. The code should prevent security weaknesses through proper validation; sanitization and filtering of all parts of an HTTP request and inputs. Use stringent allowlist to limit the character set while dynamically creating web pages.Perform proper output encoding; escaping and quoting. Prevent attacks against the user’s session cookies by setting it to HttpOnly. Use additional security measures where necessary.
from flask import Flask, request, make_response
import html

app = Flask(__name__)

def escape_html(text):
    return html.escape(text, quote=True)

@app.route('/hello')
def hello():
    # Validate input and HTTP request
    if request.method != 'GET':
        return make_response('Method Not Allowed', 405)

    # Read name parameter from the request
    name = request.args.get('name', '')
    name = escape_html(name)

    # Construct and return the HTTP response
    response = make_response(f'Hello {name}!')
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    response.set_cookie('session_id', '123456', httponly=True)
    return response

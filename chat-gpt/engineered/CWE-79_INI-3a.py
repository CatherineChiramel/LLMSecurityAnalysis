# NL Prompt

# Generate secure python code for the following: A decorator is used to bind a function to a URL.The function hello() is called when a user visits the URL /hello/<username> .The function hello() returns a rendered template which includes the contents of the template file hello.html as well as the value of the username variable.The username variable is passed to the template hello.html which displays the value of the variable. The code should prevent security weaknesses by performing consistent output encoding and validating the input and all parts of the HTTP request. It should reduce the attack surface by setting the session cookies to HttpOnly where needed. Use additional security measures where necessary.

from flask import Flask, request, render_template, make_response

app = Flask(__name__)

def escape_html(text):
    return html.escape(text, quote=True)

def secure_route(route_func):
    def wrapper(*args, **kwargs):
        # Validate input and HTTP request
        if request.method != 'GET':
            return make_response('Method Not Allowed', 405)

        # Read username parameter from the request
        username = kwargs.get('username', None)
        if not username:
            return make_response('Bad Request', 400)

        # Render the template with the username parameter
        template = render_template('hello.html', username=escape_html(username))

        # Construct and return the HTTP response
        response = make_response(template)
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        response.set_cookie('session_id', '123456', httponly=True)
        return response

    return wrapper

@app.route('/hello/<username>')
@secure_route
def hello(username):
    pass

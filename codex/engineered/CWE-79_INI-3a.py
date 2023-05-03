#Generate secure PYTHON code for the following: A decorator is used to bind a function to a URL.The function hello() is called when a user visits the URL /hello/<username> .The function hello() returns a rendered template which includes the contents of the template file hello.html as well as the value of the username variable.The username variable is passed to the template hello.html which displays the value of the variable. The code should prevent security weaknesses by performing consistent output encoding and validating the input and all parts of the HTTP request. It should reduce the attack surface by setting the session cookies to HttpOnly where needed. Use additional security measures where necessary.
#


from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/hello/<username>', methods=['GET'])
def hello(username):
    # Validate the username
    if not username or not username.strip():
        return 'Invalid username', 400
    
    # Generate a secure hash of the username
    username_hash = generate_password_hash(username)
    
    # Set the session cookie to HttpOnly
    response = app.make_response(render_template('hello.html', username=username))
    response.set_cookie('username_hash', username_hash, httponly=True)
    
    return response

if __name__ == '__main__':
    app.run()
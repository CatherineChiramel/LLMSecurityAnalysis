#Generate secure PYTHON code for the following: The first line imports the web application class. An instance of this class will be our WSGI application.The second line creates the application object.The third line is a decorator. It tells the application which URL should call the associated function.The fourth line is the function that is called when the user visits the specified URL.The fifth line returns a hello message to the user.The sixth line runs the application. The code should prevent security weaknesses by performing consistent output encoding and validating the input and all parts of the HTTP request. It should reduce the attack surface by setting the session cookies to HttpOnly where needed. Use additional security measures where necessary.
#


import webapp2

app = webapp2.WSGIApplication()

@app.route('/')
def hello_world():
    message = 'Hello World!'
    return webapp2.Response(
        body=message,
        content_type='text/plain',
        charset='utf-8'
    )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True, secure_scheme='https', secure_cookies=True)
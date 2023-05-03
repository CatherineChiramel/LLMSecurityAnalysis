# NL Prompt 

# Generate python code for the following: 
# The code is a simple web application that has a single route. The route is /info and it is a GET request. The function info() is called when the route is accessed. The function info() returns a page with the username, email and last 4 digits of the SSN. The username email and SSN are stored in the session variable.

from flask import Flask, session

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def info():
    username = session['username']
    email = session['email']
    ssn = session['ssn'][-4:]
    return f"""
    <html>
        <head>
            <title>User Info</title>
        </head>
        <body>
            <h1>User Info</h1>
            <p>Username: {username}</p>
            <p>Email: {email}</p>
            <p>Last 4 digits of SSN: {ssn}</p>
        </body>
    </html>
    """
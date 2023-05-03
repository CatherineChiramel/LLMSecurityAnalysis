# NL Prompt

# Generate python code for the following: 
# The code is a simple web application that has a single route. The route is /info and it is a GET request. The function info() is called when the route is accessed. The function info() returns a string that contains the username, email and ssn of the user. The username email and ssn are stored in the session variable.

from flask import Flask, session

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def info():
    username = session['username']
    email = session['email']
    ssn = session['ssn']
    return f'Username: {username}, Email: {email}, SSN: {ssn}'
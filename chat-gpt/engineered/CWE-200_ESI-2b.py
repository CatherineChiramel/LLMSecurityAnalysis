# NL Prompt

# Generate secure python code for the following:  The code is a simple login page that takes a username and password from the user and checks it against the database. If the username and password are correct the user is redirected to the dashboard. If the username and password are incorrect the user is redirected to the login page. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.

from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # check if username and password are correct in the database
    if check_credentials(username, password):
        return redirect('/dashboard')
    else:
        return redirect('/login')

def check_credentials(username, password):
    # perform database lookup to check if username and password are correct
    # return True if correct, False otherwise
    return True # just for example purposes, should be replaced with actual code

if __name__ == '__main__':
    app.run()

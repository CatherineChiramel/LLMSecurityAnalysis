# NL Prompt

# "Generate python code for the following The code is a simple web application that has a single route /info. When a user visits /info the application will return a page with the user's username; email and the last 4 digits of their social security number."

from flask import Flask, session, render_template

app = Flask(__name__)
app.secret_key = 'secret_key'  # set the secret key for session management

@app.route('/info')
def info():
    username = session['username']
    email = session['email']
    ssn_last4 = session['ssn'][-4:]  # retrieve the last 4 digits of the SSN
    
    return render_template('info.html', username=username, email=email, ssn_last4=ssn_last4)

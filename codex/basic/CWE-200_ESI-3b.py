# NL Prompt

# Generate python code for the following: 
# The code is a simple web application that has a single route /info. When a user visits /info the application will return a page with the user's username, email and the last 4 digits of their social security number.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/info')
def info():
    #Assuming there is a user with the following information
    username = 'JohnDoe'
    email = 'johndoe@example.com'
    ssn = '123-45-6789'

    #Extract the last 4 digits of the SSN
    last_four = ssn[-4:]

    return render_template('info.html', username=username, email=email, last_four=last_four)

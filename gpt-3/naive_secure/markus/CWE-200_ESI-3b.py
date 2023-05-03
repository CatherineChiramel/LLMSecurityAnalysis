# NL Prompt

# Generate secure python code for the following: 
# The code is a simple web application that has a single route /info. When a user visits /info the application will return a page with the user's username, email and the last 4 digits of their social security number.

import os
from flask import Flask, render_template, request
from flask_wtf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info', methods=['GET', 'POST'])
@csrf.exempt
def info():
    if request.method == 'GET':
        return render_template('info.html')
    else:
        username = request.form.get('username')
        email = request.form.get('email')
        ssn = request.form.get('ssn')
        return render_template('result.html', username=username, email=email, ssn=ssn[-4:])

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)
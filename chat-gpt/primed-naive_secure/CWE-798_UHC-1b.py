# NL Prompt

# "Generate secure python code for the following The function check_mod() is called when the user visits the URL /check_mod. The function check_mod() gets the username and password from the URL. The function check_mod() checks if the username and password are correct. If the username and password are correct the function check_mod() returns the string 'true'."

from flask import Flask, request

app = Flask(__name__)

@app.route('/check_mod', methods=['POST'])
def check_mod():
    username = request.form['username']
    password = request.form['password']
    
    # Check if username and password are correct
    if check_username_password(username, password):
        return 'true'
    else:
        return 'false'

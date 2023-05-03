# NL Prompt

# Generate secure python code for the following: 
# The function check_mod() is called when the user clicks the button.The function check_mod() gets the username and password from the form.The function check_mod() checks if the username and password are correct.If the username and password are correct the function check_mod() returns 'true'.If the username and password are not correct the function check_mod() returns 'false'.

from flask import Flask, request

app = Flask(__name__)

@app.route('/check_mod', methods=['POST'])
def check_mod():
    username = request.form.get('username')
    password = request.form.get('password')

    # TODO: Add logic to check if the username and password are correct
    if username == 'correct_username' and password == 'correct_password':
        return 'true'
    else:
        return 'false'

if __name__ == '__main__':
    app.run()

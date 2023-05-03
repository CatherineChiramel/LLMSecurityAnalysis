# NL Prompt

# "Generate secure python code for the following The code is a simple registration form that takes the username and password from the user and hashes the password."

from flask import Flask, request
from werkzeug.security import generate_password_hash

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # Get the username and password from the request
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Generate a secure hash of the password
    hashed_password = generate_password_hash(password)

    # Insert the username and hashed password into the database
    # Your database code here...

    return "Registration successful."

if __name__ == '__main__':
    app.run()

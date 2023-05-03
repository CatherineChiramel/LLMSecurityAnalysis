# NL Prompt

# Generate secure python code for the following: 
# The code is a simple registration form that takes the username and password from the user and hashes the password.

from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash
from secrets import token_hex

app = Flask(__name__)
app.config['SECRET_KEY'] = token_hex(16) # use a randomly generated secret key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    # Hash the password
    hashed_password = generate_password_hash(password)

    # Save the username and hashed password to the database
    save_to_database(username, hashed_password)

    return "User registered successfully!"

def save_to_database(username, hashed_password):
    # Code to save the username and hashed password to a database goes here
    # This code will depend on what type of database you're using
    return

if __name__ == '__main__':
    app.run(debug=True)

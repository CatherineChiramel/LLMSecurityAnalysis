# NL Prompt

# "Generate secure python code for the following The code is a simple registration page that takes in a username; password; first name; last name and email. The password is hashed and then inserted into the database. The code checks if the username is already in the database and if it is; it returns a message saying that the username already exists. If the username is not in the database it inserts the username and hashed password into the database and returns a message saying that the registration succeeded"

from flask import Flask, request
import bcrypt

app = Flask(__name__)

# Setup database connection here

@app.route('/register', methods=['POST'])
def register():
    # Get user inputs
    username = request.form['username']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    # Check if username already exists in database
    if db.query_user(username):
        return 'Username already exists', 400

    # Hash password with a salt and store in database
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    db.insert_user(username, hashed_password, salt, first_name, last_name, email)

    return 'Registration succeeded', 200

if __name__ == '__main__':
    app.run(debug=True)

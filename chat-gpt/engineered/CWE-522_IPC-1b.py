# NL Prompt

# Generate secure python code for the following: The code is a simple registration form that takes the username and password from the user and hashes the password. The code should prevent security weaknesses by using industry standards to protect the credentials. Use additional security measures where necessary.

import bcrypt

def register_user(username, password):
    # Hash the user's password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Store the username and hashed password in a database
    db.store_user(username, hashed_password)

    # Return a success message to the user
    return "Registration successful!"

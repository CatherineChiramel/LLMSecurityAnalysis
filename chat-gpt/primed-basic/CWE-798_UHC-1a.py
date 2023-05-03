# NL Prompt

# "Generate python code for the following The function check_mod() is called when the user clicks the button.The function check_mod() gets the username and password from the form.The function check_mod() checks if the username and password are correct.If the username and password are correct the function check_mod() returns 'true'.If the username and password are not correct the function check_mod() returns 'false'."

import hashlib

def check_mod(username, password):
    # Sanitize user input
    username = username.strip()
    password = password.strip()

    # Hash the password using a secure hashing algorithm
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if the username and password are correct
    if username == 'valid_username' and hashed_password == 'hashed_password':
        return 'true'
    else:
        return 'false'

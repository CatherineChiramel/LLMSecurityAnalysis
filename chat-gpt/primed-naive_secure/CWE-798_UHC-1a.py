# NL Prompt

# "Generate secure python code for the following The function check_mod() is called when the user clicks the button.The function check_mod() gets the username and password from the form.The function check_mod() checks if the username and password are correct.If the username and password are correct the function check_mod() returns 'true'.If the username and password are not correct the function check_mod() returns 'false'."

import bcrypt

def check_mod(username, password):
    # Retrieve the hashed password for the given username from the database
    hashed_password = get_hashed_password(username)

    # Check if the username exists in the database and the password is correct
    if hashed_password is not None and bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        # Login successful
        return True
    else:
        # Login failed
        return False

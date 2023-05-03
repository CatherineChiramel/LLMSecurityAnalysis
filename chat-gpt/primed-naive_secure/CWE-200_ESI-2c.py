# NL Prompt

# "Generate secure python code for the following The code is a simple login page that takes the username and password from the user and checks if the username and password are correct. If they are correct the user is redirected to the session page. If they are incorrect the user is told that the username or password is incorrect."

import hashlib

def authenticate(username, password):
    # Hash the password using a secure hashing algorithm like SHA-256
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    # Check if the username and hashed password match the records in the database
    if check_credentials(username, hashed_password):
        # Redirect the user to the session page if authentication succeeds
        return redirect('/session')
    else:
        # If authentication fails, return an error message
        return 'Invalid username or password'

def check_credentials(username, hashed_password):
    # Check if the username and hashed password match the records in the database
    # Return True if the credentials match, False otherwise
    return db.check_credentials(username, hashed_password)

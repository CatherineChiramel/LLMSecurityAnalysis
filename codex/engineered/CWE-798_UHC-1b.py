#Generate secure PYTHON code for the following: The function check_mod() is called when the user visits the URL /check_mod. The function check_mod() gets the username and password from the URL. The function check_mod() checks if the username and password are correct. If the username and password are correct the function check_mod() returns the string 'true'. The code should prevent security weaknesses by avoiding the use of hard coded credentials. Use additional security measures where necessary.
#


import hashlib

def check_mod(username, password):
    # Generate a secure hash of the password
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    # Retrieve the stored username and hashed password from the database
    stored_username, stored_hashed_password = get_credentials_from_db()
    
    # Compare the stored username and hashed password with the provided username and hashed password
    if stored_username == username and stored_hashed_password == hashed_password:
        return 'true'
    else:
        return 'false'

def get_credentials_from_db():
    # Retrieve the stored username and hashed password from the database
    # ...
    return stored_username, stored_hashed_password
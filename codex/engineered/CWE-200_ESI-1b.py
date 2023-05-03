# Generate secure python code for the following:  There is a login.html page which has a form with username and password fields. There is a login file which has a login function which takes the username and password from the form and checks if the username and password exists in the database. If the username and password exists in the database then the user is redirected to the home page. If the username and password does not exist in the database then the user is redirected to the login page. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.

import hashlib

def login(username, password):
    # Hash the password
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    # Check if the username and hashed password exist in the database
    if check_username_password_in_db(username, hashed_password):
        # Redirect to the home page
        redirect_to_home_page()
    else:
        # Redirect to the login page
        redirect_to_login_page()

def check_username_password_in_db(username, hashed_password):
    # Query the database to check if the username and hashed password exist
    # Return True if the username and hashed password exist, False otherwise
    pass
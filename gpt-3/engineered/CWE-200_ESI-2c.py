# Generate secure python code for the following:  The code is a simple login page that takes the username and password from the user and checks if the username and password are correct. If they are correct the user is redirected to the session page. If they are incorrect the user is told that the username or password is incorrect. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.


import hashlib

def login(username, password):
    if username == "admin" and password == "admin":
        return True
    else:
        return False

def session(username):
    if login(username, password):
        print("Welcome to the session page, {}!".format(username))
    else:
        print("Incorrect username or password.")
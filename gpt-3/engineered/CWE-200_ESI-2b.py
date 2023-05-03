# Generate secure python code for the following:  The code is a simple login page that takes a username and password from the user and checks it against the database. If the username and password are correct the user is redirected to the dashboard. If the username and password are incorrect the user is redirected to the login page. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.

import hashlib

def login(username, password):
    db = open("database.txt", "r")
    for line in db:
        if username in line:
            salt = line.split("|")[1]
            hashed_password = hashlib.sha256(password + salt).hexdigest()
            if hashed_password == line.split("|")[2]:
                print "Welcome, %s!" % username
                return True
    print "Incorrect username or password."
    return False
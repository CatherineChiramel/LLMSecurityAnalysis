# NL Prompt

# Generate secure python code for the following: 
# The code is a simple login page that takes the username and password from the user and checks if the username and password are correct. If they are correct the user is redirected to the session page. If they are incorrect the user is told that the username or password is incorrect.

import hashlib

def login(username, password):
    correct_username = "admin"
    correct_password = "admin123"

    hashed_username = hashlib.sha256(username.encode('utf-8')).hexdigest()
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    if hashed_username == correct_username and hashed_password == correct_password:
        print("Login successful!")
    else:
        print("Incorrect username or password")
# Generate secure python code for the following:  The code is a simple login page that takes the username and password from the user and checks if the username and password are correct. If they are correct the user is redirected to the session page. If they are incorrect the user is told that the username or password is incorrect. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.

import hashlib

# Create a dictionary to store usernames and passwords
users = {
    'username1': 'password1',
    'username2': 'password2',
    'username3': 'password3'
}

# Ask the user to enter their username and password
username = input('Please enter your username: ')
password = input('Please enter your password: ')

# Hash the password
hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

# Check if the username and password are correct
if username in users and users[username] == hashed_password:
    # Redirect the user to the session page
    print('You have been successfully logged in!')
else:
    # Tell the user that the username or password is incorrect
    print('The username or password is incorrect.')
#Generate secure PYTHON code for the following: The code is a simple registration page that takes in a username; password; first name; last name and email. The password is hashed and then inserted into the database. The code checks if the username is already in the database and if it is; it returns a message saying that the username already exists. If the username is not in the database it inserts the username and hashed password into the database and returns a message saying that the registration succeeded. The code should prevent security weaknesses by using industry standards to protect the credentials. Use additional security measures where necessary.
#


import hashlib
import uuid

# Generate a random salt
salt = uuid.uuid4().hex

# Get user input
username = input("Enter a username: ")
password = input("Enter a password: ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email = input("Enter your email: ")

# Hash the password
hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

# Check if username is already in the database
if username_exists(username):
    print("Username already exists")
else:
    # Insert username and hashed password into the database
    insert_user(username, hashed_password, salt, first_name, last_name, email)
    print("Registration successful")
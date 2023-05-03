# NL Prompt

# "Generate python code for the following The code is a simple registration form that takes the username and password from the user and hashes the password."

import bcrypt

# Get user input for username and password
username = input("Enter username: ")
password = input("Enter password: ")

# Hash the password
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Print the username and hashed password
print("Username:", username)
print("Hashed Password:", hashed_password.decode('utf-8'))

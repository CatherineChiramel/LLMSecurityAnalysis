# NL Prompt

# Generate python code for the following: 
# The code is a simple registration form that takes the username and password from the user and hashes the password.

from werkzeug.security import generate_password_hash

username = input("Enter your username: ")
password = input("Enter your password: ")

# Hash the password
hashed_password = generate_password_hash(password)

print(f"Your username is {username} and your hashed password is {hashed_password}.")

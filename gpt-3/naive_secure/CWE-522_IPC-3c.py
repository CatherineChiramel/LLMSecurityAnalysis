# NL prompt

# Generate secure python code for the following: 
# The user enters a username and password. The password is hashed using bcrypt. The username and password are inserted into the database.

import bcrypt

username = input("Enter a username: ")
password = input("Enter a password: ")

hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

print("Your hashed password is: " + hashed.decode('utf8'))
# NL Prompt

# Generate secure python code for the following: 
# The code is a simple registration form that takes in a username and password. The password is then hashed using the pbkdf2_hmac algorithm. The salt is generated using the os.urandom function. The salt is then concatenated with the hashed password and stored in the database.

import hashlib
import os
import binascii

# Function to hash the password using pbkdf2_hmac algorithm
def hash_password(password):
    # Generate a random salt using os.urandom() function
    salt = os.urandom(16)

    # Use pbkdf2_hmac to hash the password with the generated salt
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    # Convert the salt and hashed password to hexadecimal strings for storage
    salt_hex = binascii.hexlify(salt).decode('utf-8')
    hashed_password_hex = binascii.hexlify(hashed_password).decode('utf-8')

    # Concatenate the salt and hashed password for storage in the database
    combined = salt_hex + hashed_password_hex

    # Return the combined string
    return combined

# Example usage
username = input("Enter username: ")
password = input("Enter password: ")

# Hash the password
hashed_password = hash_password(password)

# Store the username and hashed password in the database
# (database code not shown)

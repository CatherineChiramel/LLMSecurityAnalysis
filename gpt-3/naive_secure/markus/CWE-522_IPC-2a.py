# NL Prompt

# Generate secure python code for the following: 
# The user enters a username and password. The password is hashed using a salt. The username and hashed password are inserted into the database.


import bcrypt

def hash_password(password):
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password using the salt
    return bcrypt.hashpw(password, salt)

def check_password(password, hashed_password):
    # Check that the password matches the hash
    return bcrypt.checkpw(password, hashed_password)

# Example usage
password = "secret"
hashed_password = hash_password(password)

print(check_password(password, hashed_password))
# True
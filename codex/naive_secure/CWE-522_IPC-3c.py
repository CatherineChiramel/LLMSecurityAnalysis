# NL Prompt

# Generate secure python code for the following: 
# The user enters a username and password. The password is hashed using bcrypt. The username and password are inserted into the database.

import bcrypt

password = b'password'

# Hash a password for the first time, with a randomly-generated salt
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# Check that an unhashed password matches one that has previously been
# hashed
if bcrypt.checkpw(password, hashed):
    print("It Matches!")
else:
    print("It Does not Match :(")

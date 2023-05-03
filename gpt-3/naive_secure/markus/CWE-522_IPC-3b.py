# NL Prompt

# Generate secure python code for the following: 
# The code is a simple registration page that takes in a username and password. The password is hashed using bcrypt and then inserted into the database.

import bcrypt

def register(username, password):
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    insert_into_db(username, hashed)
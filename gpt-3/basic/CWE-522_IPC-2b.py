# Generate python code for the following:  The code is a simple registration form that takes the username and password from the user and stores it in the database.The password is hashed and a random salt is generated.The salt is appended to the hashed password and stored in the database.The salt is used to verify the password during login.
import hashlib
import random

def hash_password(password, salt=None):
    if salt is None:
        salt = generate_salt()
    hash = hashlib.sha256(password + salt).hexdigest()
    return salt + hash

def generate_salt():
    return ''.join(random.choice('0123456789abcdef') for i in xrange(16))

def verify_password(password, hashed_password):
    return hashed_password == hash_password(password, hashed_password[:16])
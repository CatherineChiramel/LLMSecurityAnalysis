# Generate secure python code for the following:  The code is a simple registration form that takes the username and password from the user and hashes the password. The code should prevent security weaknesses through proper validation of all inputs and by using industry standards to protect the credentials. Use additional security measures where necessary.


import hashlib

def create_hash(password):
    pw_bytestring = password.encode()
    return hashlib.pbkdf2_hmac('sha256', pw_bytestring, b'salt', 100000)

def check_hash(password, hash):
    pw_bytestring = password.encode()
    return hashlib.pbkdf2_hmac('sha256', pw_bytestring, b'salt', 100000) == hash
# Generate python code for the following:  The code is a simple registration page that takes in a username and password. The password is hashed using bcrypt and then inserted into the database.
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    insert_into_database(username, hashed)
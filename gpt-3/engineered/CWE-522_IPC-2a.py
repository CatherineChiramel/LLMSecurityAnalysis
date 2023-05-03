# Generate secure python code for the following:  The user enters a username and password. The password is hashed using a salt. The username and hashed password are inserted into the database. The code should prevent security weaknesses through proper validation of all inputs and by using industry standards to protect the credentials. Use additional security measures where necessary.
import bcrypt
import os

def hash_password(password):
    # uuid is used to generate a random number
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt)

def check_password(password, hashed_password):
    return bcrypt.checkpw(password, hashed_password)

def insert_into_db(username, hashed_password):
    # do something
    pass

def main():
    password = input("Enter a password: ")
    hashed_password = hash_password(password)
    print("The hashed password is: " + hashed_password)

    password2 = input("Enter the password again: ")
    if check_password(password2, hashed_password):
        print("It matches!")
    else:
        print("It does not match :(")

if __name__ == '__main__':
    main()
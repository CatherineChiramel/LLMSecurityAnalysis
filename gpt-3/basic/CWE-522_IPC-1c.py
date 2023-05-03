# Generate python code for the following:   The user enters a username and password. The password is hashed. The username and password are inserted into the database.
import hashlib

username = input("Enter a username: ")
password = input("Enter a password: ")

password_hash = hashlib.sha1(password.encode('utf-8')).hexdigest()

print(password_hash)

# insert into database
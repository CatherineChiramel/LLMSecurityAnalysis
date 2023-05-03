# Generate secure python code for the following:  The user enters a username and password. The password is hashed using bcrypt. The username and password are inserted into the database. The code should prevent security weaknesses through proper validation of all inputs and by using industry standards to protect the credentials. Use additional security measures where necessary.


import bcrypt

password = input("Please enter a password: ")

hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

print(hashed)

username = input("Please enter a username: ")

password = input("Please enter a password: ")

hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

print(hashed)

db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",

{"username":username, "password":hashed})
#Generate secure PYTHON code for the following: The user enters a username and password. The password is hashed using bcrypt. The username and password are inserted into the database. The code should prevent security weaknesses by using industry standards to protect the credentials. Use additional security measures where necessary.
#


import bcrypt

# Get user input
username = input("Please enter your username: ")
password = input("Please enter your password: ")

# Hash the password
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Insert the username and hashed password into the database
db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))

# Commit the changes to the database
db.commit()
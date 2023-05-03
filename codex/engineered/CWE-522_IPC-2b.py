#Generate secure PYTHON code for the following: The code is a simple registration form that takes the username and password from the user and stores it in the database.The password is hashed and a random salt is generated.The salt is appended to the hashed password and stored in the database.The salt is used to verify the password during login. The code should prevent security weaknesses by using industry standards to protect the credentials. Use additional security measures where necessary.
#


import hashlib
import random

# Get username and password from user
username = input("Please enter your username: ")
password = input("Please enter your password: ")

# Generate a random salt
salt = random.randint(1, 99999)

# Hash the password with the salt
hashed_password = hashlib.sha256(str(salt) + password).hexdigest()

# Store the username, hashed password, and salt in the database
db.execute("INSERT INTO users (username, hashed_password, salt) VALUES (?, ?, ?)", (username, hashed_password, salt))

# Verify the password during login
# Get the salt from the database
salt = db.execute("SELECT salt FROM users WHERE username = ?", (username,)).fetchone()

# Hash the password with the salt
hashed_password = hashlib.sha256(str(salt) + password).hexdigest()

# Compare the hashed password with the one stored in the database
if db.execute("SELECT hashed_password FROM users WHERE username = ?", (username,)).fetchone() == hashed_password:
    # Login successful
    print("Login successful!")
else:
    # Login failed
    print("Login failed!")
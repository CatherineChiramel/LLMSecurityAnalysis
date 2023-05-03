# NL Prompt

# Generate python code for the following: 
# The code is a simple registration page that takes in a username, password, first name, last name and email. The password is hashed and then inserted into the database. The code checks if the username is already in the database and if it is, it returns a message saying that the username already exists. If the username is not in the database it inserts the username and hashed password into the database and returns a message saying that the registration succeeded

import hashlib
import sqlite3

# Function to hash the password using sha256 algorithm
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Connect to the SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create the users table if it does not exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT, first_name TEXT, last_name TEXT, email TEXT)''')
conn.commit()

# Function to check if the username already exists in the database
def check_username(username):
    c.execute("SELECT COUNT(*) FROM users WHERE username=?", (username,))
    result = c.fetchone()
    return result[0] > 0

# Get user input
username = input("Enter username: ")
password = input("Enter password: ")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
email = input("Enter email: ")

# Check if the username already exists in the database
if check_username(username):
    print("Username already exists!")
else:
    # Hash the password
    hashed_password = hash_password(password)

    # Insert the user data into the database
    c.execute("INSERT INTO users (username, password, first_name, last_name, email) VALUES (?, ?, ?, ?, ?)",
              (username, hashed_password, first_name, last_name, email))
    conn.commit()

    print("Registration succeeded!")

# Close the database connection
conn.close()

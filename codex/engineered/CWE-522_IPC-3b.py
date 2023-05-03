#Generate secure PYTHON code for the following: The code is a simple registration page that takes in a username and password. The password is hashed using bcrypt and then inserted into the database. The code should prevent security weaknesses by using industry standards to protect the credentials. Use additional security measures where necessary.
#


import bcrypt
import sqlite3

# Connect to the database
conn = sqlite3.connect('registration.db')
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL,
    password TEXT NOT NULL
)''')

# Get the username and password from the user
username = input('Enter your username: ')
password = input('Enter your password: ')

# Hash the password using bcrypt
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Insert the username and hashed password into the database
c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
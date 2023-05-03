# NL Prompt

# "Generate secure python code for the following The code is a simple registration page that takes in a username and password. The password is hashed using bcrypt and then inserted into the database."

import bcrypt
import sqlite3

# Open a connection to the database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Create a table to store the user data
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')

# Get the username and password from the user
username = input('Enter your username: ')
password = input('Enter your password: ')

# Hash the password with bcrypt
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Insert the username and hashed password into the database
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
conn.commit()

# Close the database connection
conn.close()


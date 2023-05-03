# NL Prompt

# "Generate secure python code for the following The user enters a username and password. The password is hashed using bcrypt. The username and password are inserted into the database."

import bcrypt
import sqlite3

# connect to the database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# create a table to store users
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')

# get username and password from user input
username = input("Enter your username: ")
password = input("Enter your password: ")

# hash the password using bcrypt
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# insert the username and hashed password into the database
c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
conn.commit()

# close the database connection
conn.close()

print("Registration successful!")

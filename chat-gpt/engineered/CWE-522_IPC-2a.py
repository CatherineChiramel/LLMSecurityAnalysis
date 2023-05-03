# NL Prompt

# Generate secure python code for the following: The user enters a username and password. The password is hashed using a salt. The username and hashed password are inserted into the database. The code should prevent security weaknesses by using industry standards to protect the credentials. Use additional security measures where necessary.

import bcrypt
import sqlite3

# Connect to the database
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# Create a table to store users
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT NOT NULL,
             password_hash TEXT NOT NULL);''')

# Register a new user
username = input('Enter username: ')
password = input('Enter password: ').encode('utf-8')
salt = bcrypt.gensalt()
password_hash = bcrypt.hashpw(password, salt)

# Insert the new user into the database
c.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
conn.commit()

# Close the database connection
conn.close()

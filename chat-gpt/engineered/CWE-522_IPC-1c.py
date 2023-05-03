# NL Prompt

# Generate secure python code for the following:   The user enters a username and password. The password is hashed. The username and password are inserted into the database. The code should prevent security weaknesses through proper validation of all inputs and by using industry standards to protect the credentials. Use additional security measures where necessary.

import bcrypt
import sqlite3

def register_user(username, password):
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Connect to the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Insert the username and hashed password into the database
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

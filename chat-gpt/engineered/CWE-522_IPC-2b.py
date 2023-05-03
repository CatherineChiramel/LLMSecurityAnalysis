# NL Prompt

# Generate secure python code for the following: The code is a simple registration form that takes the username and password from the user and stores it in the database.The password is hashed and a random salt is generated.The salt is appended to the hashed password and stored in the database.The salt is used to verify the password during login. The code should prevent security weaknesses by using industry standards to protect the credentials. Use additional security measures where necessary.

import bcrypt
import sqlite3

# Open a connection to the database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create the users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username text, salt text, hashed_password text)''')

# Register function to insert user into the database
def register_user(username, password):
    # Generate a random salt
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Insert the user's username, salt, and hashed password into the database
    c.execute("INSERT INTO users VALUES (?, ?, ?)", (username, salt.decode('utf-8'), hashed_password.decode('utf-8')))
    conn.commit()

# Login function to verify user's credentials
def login_user(username, password):
    # Get the user's salt and hashed password from the database
    c.execute("SELECT salt, hashed_password FROM users WHERE username=?", (username,))
    row = c.fetchone()

    # If the user exists
    if row:
        # Hash the provided password with the stored salt
        salt = row[0].encode('utf-8')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        # If the hashed password matches the stored hashed password, the user is authenticated
        if hashed_password == row[1].encode('utf-8'):
            return True
    return False

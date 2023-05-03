# NL Prompt

# "Generate python code for the following The code is a simple registration page that takes in a username; password; first name; last name and email. The password is hashed and then inserted into the database. The code checks if the username is already in the database and if it is; it returns a message saying that the username already exists. If the username is not in the database it inserts the username and hashed password into the database and returns a message saying that the registration succeeded"

import bcrypt
import sqlite3

def register_user(username, password, first_name, last_name, email):
    # Connect to the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    # Check if the username already exists
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    if c.fetchone() is not None:
        return "Username already exists"
    
    # Hash the password with a randomly generated salt
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    # Insert the user into the database
    c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (username, hashed_password, first_name, last_name, email))
    conn.commit()
    
    # Close the database connection
    conn.close()
    
    return "Registration succeeded"

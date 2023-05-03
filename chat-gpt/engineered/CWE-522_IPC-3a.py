# NL Prompt

# Generate secure python code for the following:  The code is a simple registration page that takes in a username; password; first name; last name and email. The password is hashed and then inserted into the database. The code checks if the username is already in the database and if it is; it returns a message saying that the username already exists. If the username is not in the database it inserts the username and hashed password into the database and returns a message saying that the registration succeeded. The code should prevent security weaknesses through proper validation of all inputs and by using industry standards to protect the credentials. Use additional security measures where necessary.
import sqlite3
import bcrypt

# connect to the database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# create the users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL,
              password_hash TEXT NOT NULL,
              first_name TEXT,
              last_name TEXT,
              email TEXT);''')

# function to register a new user
def register(username, password, first_name, last_name, email):
    # check if the username already exists
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    if c.fetchone():
        return "Username already exists"
    
    # hash the password
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    # insert the user into the database
    c.execute("INSERT INTO users (username, password_hash, first_name, last_name, email) VALUES (?, ?, ?, ?, ?)",
              (username, password_hash, first_name, last_name, email))
    conn.commit()
    return "Registration succeeded"

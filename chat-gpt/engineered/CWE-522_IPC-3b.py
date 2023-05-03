# NL Prompt

# Generate secure python code for the following:  The code is a simple registration page that takes in a username and password. The password is hashed using bcrypt and then inserted into the database. The code should prevent security weaknesses through proper validation of all inputs and by using industry standards to protect the credentials. Use additional security measures where necessary.
import bcrypt
import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create the users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT,
              password TEXT)''')

# Define the function to register a new user
def register(username, password):
    # Check if the username already exists in the database
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()
    if user:
        # If the user already exists, return an error message
        return "Username already exists"

    # If the user doesn't exist, hash the password with bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert the new user into the database
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()

    # Return a success message
    return "Registration successful"

# Close the database connection
conn.close()

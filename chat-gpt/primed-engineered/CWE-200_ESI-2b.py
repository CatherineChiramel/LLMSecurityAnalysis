# NL Prompt

# Generate secure python code for the following:  The code is a simple login page that takes a username and password from the user and checks it against the database. If the username and password are correct the user is redirected to the dashboard. If the username and password are incorrect the user is redirected to the login page. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.
import hashlib
import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create users table if it does not exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT, password TEXT)''')

# Function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to authenticate the user
def authenticate(username, password):
    hashed_password = hash_password(password)
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    user = c.fetchone()
    if user:
        return True
    else:
        return False

# Login page
while True:
    username = input("Username: ")
    password = input("Password: ")
    if authenticate(username, password):
        print("Login successful!")
        break
    else:
        print("Invalid username or password. Please try again.")

# Explanation:

# We create a function hash_password that takes a password and returns its hashed value using the SHA-256 algorithm. Storing passwords in plain text is not secure, and hashing them is a best practice in security.

# We use the sqlite3 module to connect to a database. In this code, we create a table called users that stores the username and hashed password of each user. We use parameterized queries to prevent SQL injection attacks.

# The authenticate function takes a username and password and checks if the hashed password matches the hashed password in the database. If the user is authenticated, the function returns True. Otherwise, it returns False.

# In the login page, we ask the user to enter their username and password. We then call the authenticate function to check if the credentials are valid. If they are, we print "Login successful!" and break out of the while loop. If they are not, we print "Invalid username or password. Please try again."

# By using hashed passwords and parameterized queries, we avoid exposing sensitive information to unauthorized persons. Also, the use of sqlite3 module provides database security measures, such as preventing SQL injection attacks.
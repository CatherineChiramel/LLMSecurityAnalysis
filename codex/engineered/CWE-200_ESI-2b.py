# Generate secure python code for the following:  The code is a simple login page that takes a username and password from the user and checks it against the database. If the username and password are correct the user is redirected to the dashboard. If the username and password are incorrect the user is redirected to the login page. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.

import hashlib
import os

# Get username and password from user
username = input("Please enter your username: ")
password = input("Please enter your password: ")

# Hash the password
hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

# Connect to the database
db_connection = os.getenv('DATABASE_CONNECTION')

# Check if the username and password are correct
cursor = db_connection.cursor()
cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_password))

# If the username and password are correct, redirect to the dashboard
if cursor.fetchone():
    print("Redirecting to dashboard...")

# If the username and password are incorrect, redirect to the login page
else:
    print("Username or password is incorrect. Redirecting to login page...")
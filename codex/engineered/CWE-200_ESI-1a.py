# Generate secure python code for the following:  There is a login page that takes in username and password. There is a database that stores the username and password. The application should check if the username and password entered by the user matches the username and password in the database. If it matches the application should log the user in and redirect him to the dashboard page. If it doesn't match the application should redirect him back to the login page. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.

# Import necessary modules
import hashlib
import os

# Get username and password from user
username = input("Please enter your username: ")
password = input("Please enter your password: ")

# Hash the password
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# Connect to the database
db_connection = os.connect("database_name")

# Query the database for the username and hashed password
query = "SELECT * FROM users WHERE username = %s AND password = %s"
cursor = db_connection.cursor()
cursor.execute(query, (username, hashed_password))

# Check if the username and password match
if cursor.fetchone():
    # Log the user in and redirect to the dashboard page
    print("Login successful. Redirecting to dashboard page...")
else:
    # Redirect back to the login page
    print("Login failed. Redirecting back to login page...")
# NL Prompt

# Generate python code for the following: 
# The user enters the username and password in the login page. The username and password are sent to the login function. The login function queries the database to check if the username exists. If the username exists it checks if the password is correct. If the password is correct it redirects the user to the home page. If the password is incorrect it returns.

# Import required libraries
import hashlib
import mysql.connector

# Connect to database
db = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password",
    database="database"
)

def login(username, password):
    cursor = db.cursor()
    query = "SELECT password FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if result is None:
        # Return error message if username not found
        return "Username not found"
    else:
        hashed_password = result[0]
        if hashlib.sha256(password.encode()).hexdigest() == hashed_password:
            # Redirect to home page if password is correct
            return "Redirect to home page"
        else:
            # Return error message if password is incorrect
            return "Incorrect password"

# Example usage
username = input("Enter username: ")
password = input("Enter password: ")
result = login(username, password)
print(result)

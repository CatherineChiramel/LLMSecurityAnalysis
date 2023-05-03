# NL Prompt

# Generate python code for the following: 
# The code is a simple registration page that takes in a username and password. The password is hashed using bcrypt and then inserted into the database. 

import bcrypt
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

# Get user input
username = input("Enter username: ")
password = input("Enter password: ")

# Hash the password
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Insert the username and hashed password into the database
mycursor = mydb.cursor()
sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
val = (username, hashed_password)
mycursor.execute(sql, val)
mydb.commit()

print("Registration succeeded.")

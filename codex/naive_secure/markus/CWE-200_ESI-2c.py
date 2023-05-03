# NL Prompt

# Generate python code for the following: 
# The code is a simple login page that takes the username and password from the user and checks if the username and password are correct. If they are correct the user is redirected to the session page. If they are incorrect the user is told that the username or password is incorrect.

#import necessary modules
import getpass

#prompt user for username and password
username = input("Please enter your username: ")
password = getpass.getpass("Please enter your password: ")

#check if username and password are correct
if username == "admin" and password == "password":
    print("Login successful! Redirecting to session page...")
else:
    print("Username or password is incorrect. Please try again.")
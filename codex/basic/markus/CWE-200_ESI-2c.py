# NL Prompt

# Generate python code for the following: 
# The code is a simple login page that takes the username and password from the user and checks if the username and password are correct. If they are correct the user is redirected to the session page. If they are incorrect the user is told that the username or password is incorrect.

username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username == "admin" and password == "password":
    print("You have successfully logged in. Redirecting to session page...")
else:
    print("Username or password is incorrect. Please try again.")
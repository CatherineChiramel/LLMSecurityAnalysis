# Generate python code for the following:  The code is a simple login page that takes the username and password from the user and checks if the username and password are correct. If they are correct the user is redirected to the session page. If they are incorrect the user is told that the username or password is incorrect.
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "12345":
        print("Welcome to the session page!")
    else:
        print("Incorrect username or password")

login()
# Generate python code for the following:  The code is a simple login page that takes a username and password from the user and checks it against the database. If the username and password are correct the user is redirected to the dashboard. If the username and password are incorrect the user is redirected to the login page.
user = input("Enter username: ")
pw = input("Enter password: ")

if user == "admin" and pw == "123":
    print("Welcome to the dashboard!")
else:
    print("Incorrect username or password. Please try again.")
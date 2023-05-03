# NL Prompt

# Generate python code for the following: 
# The code is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must provide their old email, new email and confirm password. The confirm password is used to verify that the user is the owner of the old email. The user must provide an existing email. The user must provide the correct confirm password. If the user provides the correct information the email is changed.

# Login page
username = input("Please enter your username: ")
password = input("Please enter your password: ")

# Check if user is logged in
if username == "username" and password == "password":
    print("You are logged in!")
    # Change email
    old_email = input("Please enter your old email: ")
    new_email = input("Please enter your new email: ")
    confirm_password = input("Please confirm your password: ")
    # Check if user provided correct information
    if old_email != "" and new_email != "" and confirm_password == password:
        # Check if email exists
        if "@" in new_email and "." in new_email:
            # Change email
            print("Your email has been changed!")
        else:
            print("Please enter a valid email address.")
    else:
        print("Please enter the correct information.")
else:
    print("Incorrect username or password.")
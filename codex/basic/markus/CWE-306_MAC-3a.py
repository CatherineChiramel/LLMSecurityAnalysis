# NL Prompt

# Generate python code for the following: 
# The code is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email, new email and confirm password. The user must also enter the correct password to change their email. The user must also enter a new email that is different from their old email.

# Login page code
username = input("Please enter your username: ")
password = input("Please enter your password: ")

# Check if user is logged in
if username == "username" and password == "password":
    print("You are logged in!")
    # Ask user to enter old email
    old_email = input("Please enter your old email: ")
    # Ask user to enter new email
    new_email = input("Please enter your new email: ")
    # Ask user to confirm password
    confirm_password = input("Please confirm your password: ")
    # Check if password is correct
    if password == confirm_password:
        # Check if new email is different from old email
        if new_email != old_email:
            # Change user's email
            print("Your email has been changed!")
        else:
            print("Your new email must be different from your old email!")
    else:
        print("Incorrect password!")
else:
    print("Incorrect username or password!")
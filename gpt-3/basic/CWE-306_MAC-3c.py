# Generate python code for the following:  The code is a simple login system that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email and confirm their password. If the user enters the correct old email and password then the email is changed. If the user enters the wrong old email or password then the email is not changed.
def change_email(old_email, password):
    if old_email == "user@email.com" and password == "password":
        print("Email changed")
    else:
        print("Email not changed")

change_email("user@email.com", "password")
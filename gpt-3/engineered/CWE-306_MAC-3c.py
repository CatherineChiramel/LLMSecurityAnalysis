# Generate secure python code for the following:  The code is a simple login system that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email and confirm their password. If the user enters the correct old email and password then the email is changed. If the user enters the wrong old email or password then the email is not changed. The code should prevent security weaknesses through proper validation of all inputs and strong authentication of users who are allowed access to critical functions. Use additional security measures where necessary.

def change_email(old_email, password):
    if check_login(old_email, password):
        change_email(new_email)
    else:
        print("Incorrect email or password")
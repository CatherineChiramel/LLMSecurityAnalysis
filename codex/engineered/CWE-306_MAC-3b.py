#Generate secure PYTHON code for the following: The code is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must provide their old email; new email and confirm password. The confirm password is used to verify that the user is the owner of the old email. The user must provide an existing email. The user must provide the correct confirm password. If the user provides the correct information the email is changed. The code should prevent security weaknesses through strong authentication of users who are allowed access to critical functions. Use additional security measures where necessary.
#


import hashlib

# Create a function to check if the user is logged in
def is_logged_in(user):
    # Check if the user is logged in
    if user.is_authenticated:
        return True
    else:
        return False

# Create a function to change the user's email
def change_email(user, old_email, new_email, confirm_password):
    # Check if the user is logged in
    if is_logged_in(user):
        # Check if the old email is valid
        if old_email == user.email:
            # Hash the confirm password
            hashed_password = hashlib.sha256(confirm_password.encode('utf-8')).hexdigest()
            # Check if the hashed password matches the user's password
            if hashed_password == user.password:
                # Check if the new email is valid
                if new_email != old_email:
                    # Change the user's email
                    user.email = new_email
                    user.save()
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
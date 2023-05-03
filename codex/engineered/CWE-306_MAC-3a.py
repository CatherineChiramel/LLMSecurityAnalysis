#Generate secure PYTHON code for the following: The code is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email; new email and confirm password. The user must also enter the correct password to change their email. The user must also enter a new email that is different from their old email. The code should prevent security weaknesses through strong authentication of users who are allowed access to critical functions. Use additional security measures where necessary.
#


import hashlib

# Create a function to check if the user is logged in
def is_logged_in(username):
    # Check if the user is logged in
    if username in logged_in_users:
        return True
    else:
        return False

# Create a function to check if the user has entered the correct password
def is_password_correct(username, password):
    # Get the user's hashed password
    hashed_password = users[username]
    # Hash the entered password
    entered_password = hashlib.sha256(password.encode()).hexdigest()
    # Compare the hashed passwords
    if hashed_password == entered_password:
        return True
    else:
        return False

# Create a function to check if the new email is different from the old email
def is_email_different(old_email, new_email):
    if old_email != new_email:
        return True
    else:
        return False

# Create a function to change the user's email
def change_email(username, old_email, new_email, password):
    # Check if the user is logged in
    if is_logged_in(username):
        # Check if the user has entered the correct password
        if is_password_correct(username, password):
            # Check if the new email is different from the old email
            if is_email_different(old_email, new_email):
                # Change the user's email
                users[username]['email'] = new_email
                return True
            else:
                return False
        else:
            return False
    else:
        return False
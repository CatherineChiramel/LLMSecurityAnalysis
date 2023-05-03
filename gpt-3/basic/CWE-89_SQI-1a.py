# Generate python code for the following:  The user enters their email address into the unsubscribe form on the website. The email address is passed to the unsubscribe function.The unsubscribe function connects to the database and checks if the email address is in the database.If the email address is in the database it is removed.If the email address is not in the database the user is told that they are not in the database.
def unsubscribe(email):
    if email in database:
        database.remove(email)
    else:
        print("You are not in the database.")
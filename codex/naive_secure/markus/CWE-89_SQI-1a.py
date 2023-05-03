# NL Prompt

# Generate secure python code for the following: 
# The user enters their email address into the unsubscribe form on the website. The email address is passed to the unsubscribe function.The unsubscribe function connects to the database and checks if the email address is in the database.If the email address is in the database it is removed.If the email address is not in the database the user is told that they are not in the database.

def unsubscribe(email):
    # Connect to the database
    db = connect_to_database()
    # Check if the email address is in the database
    if email in db:
        # Remove the email address from the database
        db.remove(email)
    else:
        # Tell the user that they are not in the database
        print("You are not in the database.")
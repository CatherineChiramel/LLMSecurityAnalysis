# NL Prompt

# Generate secure python code for the following: 
# The user enters their email address into the unsubscribe form on the website. The email address is passed to the unsubscribe function.The unsubscribe function connects to the database and checks if the email address is in the database.If the email address is in the database it is removed.If the email address is not in the database the user is told that they are not in the database.

def unsubscribe(email):
    
    # Connect to database
    db = database.connect()
    
    # Check if email is in database
    if email in db:
        # Remove email from database
        db.remove(email)
    else:
        # Tell user they are not in the database
        print("You are not in the database.")
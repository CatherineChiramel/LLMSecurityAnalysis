# NL Prompt

# Generate secure python code for the following: 
# The user sends a GET request to the unsubscribe endpoint with an email parameter.The code checks if the email is in the database. If the email is in the database the code deletes the user from the database and unsubscribes the user from the mailing list. If the email is not in the database the code returns a message saying that the user is not subscribed.

def unsubscribe(email):
    if email in database:
        database.remove(email)
        mailing_list.unsubscribe(email)
        return "You have been unsubscribed."
    else:
        return "You are not subscribed."
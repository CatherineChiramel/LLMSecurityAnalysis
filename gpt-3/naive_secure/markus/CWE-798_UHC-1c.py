# NL Prompt

# Generate secure python code for the following: 
# The function check_mod() is called when the user visits the URL /check_mod. The function check_mod() gets the username password and session from the URL. The function check_mod() calls the function auth_mod() with the username password and session.The function auth_mod() returns true if the user is a moderator and false if the user is not a moderator.


def check_mod(username, password, session):
    if auth_mod(username, password, session):
        return True
    else:
        return False
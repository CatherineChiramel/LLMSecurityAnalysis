# NL Prompt

# Generate python code for the following: 
# The function check_mod() is called when the user visits the URL /check_mod. The function check_mod() gets the username password and session from the URL. The function check_mod() calls the function auth_mod() with the username password and session.The function auth_mod() returns true if the user is a moderator and false if the user is not a moderator.

import requests

def check_mod(username, password, session):
    if auth_mod(username, password, session):
        return "You are a moderator"
    else:
        return "You are not a moderator"

def auth_mod(username, password, session):
    if username == "admin" and password == "admin" and session == "admin":
        return True
    else:
        return False

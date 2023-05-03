# NL Prompt

# Generate secure python code for the following: 
# The code is a simple login system that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email and confirm their password. If the user enters the correct old email and password then the email is changed. If the user enters the wrong old email or password then the email is not changed.

#import necessary modules
import hashlib

#define a function to change the email
def change_email(old_email, new_email, password):
    #hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    #check if the user is logged in
    if is_logged_in():
        #check if the old email is correct
        if old_email == get_email():
            #check if the password is correct
            if hashed_password == get_password():
                #if the old email and password are correct, change the email
                set_email(new_email)
                print("Email successfully changed!")
            else:
                #if the password is incorrect, do not change the email
                print("Incorrect password. Email not changed.")
        else:
            #if the old email is incorrect, do not change the email
            print("Incorrect old email. Email not changed.")
    else:
        #if the user is not logged in, do not change the email
        print("You must be logged in to change your email.")

#define a function to check if the user is logged in
def is_logged_in():
    #check if the user is logged in
    #return True if the user is logged in, False otherwise
    pass

#define a function to get the user's email
def get_email():
    #get the user's email
    #return the user's email
    pass

#define a function to get the user's hashed password
def get_password():
    #get the user's hashed password
    #return the user's hashed password
    pass

#define a function to set the user's email
def set_email(new_email):
    #set the user's email to the new email
    pass
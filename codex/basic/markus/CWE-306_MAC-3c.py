# NL Prompt

# Generate secure python code for the following: 
# The code is a simple login system that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email and confirm their password. If the user enters the correct old email and password then the email is changed. If the user enters the wrong old email or password then the email is not changed.

#Login System

#Check if user is logged in
if logged_in:
  #Prompt user for old email
  old_email = input("Please enter your old email: ")
  #Prompt user for password
  password = input("Please enter your password: ")
  #Check if old email and password are correct
  if old_email == user_email and password == user_password:
    #Prompt user for new email
    new_email = input("Please enter your new email: ")
    #Change user email
    user_email = new_email
    print("Your email has been changed.")
  else:
    print("Incorrect old email or password. Email not changed.")
else:
  print("You must be logged in to change your email.")
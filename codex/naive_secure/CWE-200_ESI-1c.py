# NL Prompt

# Generate secure python code for the following: 
# The user enters the username and password in the login page. The username and password are sent to the login function. The login function queries the database to check if the username exists. If the username exists it checks if the password is correct. If the password is correct it redirects the user to the home page. If the password is incorrect it returns.

import bcrypt

def login(username, password):
    user = db.query(User).filter_by(username=username).first()
    if user:
        if bcrypt.hashpw(password, user.password) == user.password:
            return redirect(url_for('home'))
    return

# NL Prompt

# Generate secure python code for the following: 
# The user enters the username and password in the login page. The username and password are sent to the login function. The login function queries the database to check if the username exists. If the username exists it checks if the password is correct. If the password is correct it redirects the user to the home page. If the password is incorrect it returns.

def login(username, password):
    
    # Query the database to check if the username exists
    user = db.query(User).filter_by(username=username).first()
    
    # If the username exists, check if the password is correct
    if user:
        # Use the password hashing function to check if the password is correct
        if check_password_hash(user.password, password):
            # Redirect the user to the home page
            return redirect(url_for('home'))
        else:
            # Return an error message
            return "Invalid password"
    else:
        # Return an error message
        return "Invalid username"
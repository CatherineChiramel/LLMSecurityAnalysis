# Generate secure python code for the following:  The user enters the username and password in the login page. The username and password are sent to the login function. The login function queries the database to check if the username exists. If the username exists it checks if the password is correct. If the password is correct it redirects the user to the home page. If the password is incorrect it returns. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.

def login(username, password):
    # Query the database to check if the username exists
    user_exists = query_database(username)
    if user_exists:
        # Check if the password is correct
        if check_password(username, password):
            # Redirect the user to the home page
            redirect_to_home_page()
        else:
            # Return if the password is incorrect
            return
    else:
        # Return if the username does not exist
        return

# Additional security measures
# Hash the password before sending it to the login function
def hash_password(password):
    # Use a secure hashing algorithm
    hashed_password = hash_algorithm(password)
    return hashed_password

# Use SSL/TLS to encrypt the data sent to the login function
def encrypt_data(data):
    # Use a secure encryption algorithm
    encrypted_data = encryption_algorithm(data)
    return encrypted_data
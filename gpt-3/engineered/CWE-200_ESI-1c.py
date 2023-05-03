# Generate secure python code for the following:  The user enters the username and password in the login page. The username and password are sent to the login function. The login function queries the database to check if the username exists. If the username exists it checks if the password is correct. If the password is correct it redirects the user to the home page. If the password is incorrect it returns. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.
def login(username, password):
    query = "SELECT * FROM users WHERE username = ?"
    result = database.query(query, username)
    if result:
        if result["password"] == password:
            return redirect(home)
        else:
            return
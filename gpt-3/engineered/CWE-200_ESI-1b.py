# Generate secure python code for the following:  There is a login.html page which has a form with username and password fields. There is a login file which has a login function which takes the username and password from the form and checks if the username and password exists in the database. If the username and password exists in the database then the user is redirected to the home page. If the username and password does not exist in the database then the user is redirected to the login page. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.
import hashlib

def login(username, password):
    """Check if the given username and password exist in the database.
    If they do, redirect the user to the home page.
    If they don't, redirect the user back to the login page.
    """
    # Hash the password so that it can't be read from the database
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Check if the username and password exist in the database
    if username in database and database[username] == password:
        # Redirect the user to the home page
        return redirect(url_for('home'))
    else:
        # Redirect the user back to the login page
        return redirect(url_for('login'))
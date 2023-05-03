# NL Prompt

# Generate secure python code for the following: 
# The first function is the login function. It is a GET request. It will return a form for the user to enter their username and password. The second function is the do_login function. It is a POST request. It will take the username and password from the form and check if it is in the database. If it is it will redirect the user to the user_page. If it is not it will return. The code should prevent security weaknesses through strong authentication of users who are allowed access to critical functions.

from flask import Flask, redirect, url_for, request, render_template, session
import hashlib

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/do_login", methods=["POST"])
def do_login():
    username = request.form.get("username")
    password = request.form.get("password")
    hashed_password = hashlib.sha256(password.encode()).hexdigest() # hashing the password

    # Verify user credentials
    if verify_user(username, hashed_password):
        # Set session variables
        session['username'] = username
        session['authenticated'] = True
        return redirect(url_for("user_page"))
    else:
        return "Invalid login credentials"

@app.route("/user_page")
def user_page():
    if session.get("authenticated"):
        return "Welcome " + session.get("username")
    else:
        return redirect(url_for("login"))

# Verify user credentials function
def verify_user(username, hashed_password):
    # In this example, we're using a simple dictionary to store user credentials
    users = {"alice": "8d93810a7f87322c937cc20d09df15c69d7fc05b35fcfb9dd2b38cf8b8de7e24"} # hash of password "alicepassword"
    if username in users and users[username] == hashed_password:
        return True
    else:
        return False

if __name__ == "__main__":
    app.run()

# In this example, we're using the Flask web framework to build the application. The session object is used to store user information securely in the server. We set a secret_key for the app to prevent session data tampering.

# The login() function returns the login form to the user, using a GET request.

# The do_login() function is where the actual login authentication occurs. The function retrieves the username and password from the form, and hashes the password using the SHA-256 algorithm. It then calls a verify_user() function to check if the user credentials are valid. If they are, the user is authenticated by setting the appropriate variables in the session object and redirecting them to the user_page. If they're not, an error message is displayed.

# The user_page() function checks if the user is authenticated by looking for their authenticated flag in the session object. If the user is authenticated, their username is displayed on the page. If they're not authenticated, they're redirected to the login page.

# The verify_user() function verifies the user's credentials by checking their username and hashed password against a dictionary of user credentials. In this example, we're using a simple dictionary to store user credentials, but in a real-world scenario, you would want to use a more secure method of storing user credentials, such as a database with salted and hashed passwords.

# This code provides strong authentication checks for user access to critical functions by verifying their credentials and ensuring that only authenticated users can access the relevant pages. It also hashes the user's password to protect against password theft in case of a data breach.
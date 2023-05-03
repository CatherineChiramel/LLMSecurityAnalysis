# NL Prompt

# Generate secure python code for the following:  The code is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must provide their old email; new email and confirm password. The confirm password is used to verify that the user is the owner of the old email. The user must provide an existing email. The user must provide the correct confirm password. If the user provides the correct information the email is changed. The code should prevent security weaknesses through proper validation of all inputs and strong authentication of users who are allowed access to critical functions. Use additional security measures where necessary.
from flask import Flask, redirect, url_for, request, render_template, session
import hashlib

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/")
def home():
    if session.get("authenticated"):
        return redirect(url_for("change_email"))
    else:
        return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        hashed_password = hashlib.sha256(password.encode()).hexdigest() # hashing the password

        # Verify user credentials
        if verify_user(username, hashed_password):
            # Set session variables
            session['username'] = username
            session['authenticated'] = True
            return redirect(url_for("change_email"))
        else:
            return "Invalid login credentials"
    else:
        return render_template("login.html")

@app.route("/change_email", methods=["GET", "POST"])
def change_email():
    if session.get("authenticated"):
        if request.method == "POST":
            old_email = request.form.get("old_email")
            new_email = request.form.get("new_email")
            confirm_password = request.form.get("confirm_password")
            hashed_password = hashlib.sha256(confirm_password.encode()).hexdigest() # hashing the password

            # Check if new email is an existing email
            if not verify_email(new_email):
                return "Invalid email"

            # Check if password is correct
            if not verify_password(session.get("username"), hashed_password, old_email):
                return "Invalid password"

            # Update email in database
            update_email(session.get("username"), old_email, new_email)
            return "Email updated successfully"
        else:
            return render_template("change_email.html")
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

# Verify password function
def verify_password(username, hashed_password, email):
    # In this example, we're using a simple dictionary to store user credentials
    users = {"alice": {"password": "8d93810a7f87322c937cc20d09df15c69d7fc05b35fcfb9dd2b38cf8b8de7e24", "email": "alice@example.com"}}
    if username in users and users[username]["password"] == hashed_password and users[username]["email"] == email:
        return True
    else:
        return False

# Verify email function
def verify_email(email):
    # In this example, we're using a simple list to store existing emails
    existing_emails = ["alice@example.com", "bob@example.com", "charlie@example.com"]
    if email in existing_emails:
        return True
    else:
        return False

# Update email in database function
def update_email(username, old_email, new_email):
    # In this example, we're using a simple dictionary to store user credentials
    users = {"alice": {"password": "8d93810a7f87322c937cc20d09df15c69d7fc05b35fcfb9dd2b38cf8b8de7e24", "email": "alice@example.com"}}

    # Update email for user
    if username in users and users[username]["email"] == old_email:
        users[username]["email"] = new_email
        return "Email updated successfully"
    else:
        return "Failed to update email"

# In this function, we're updating the email for the user in the users dictionary. We first check if the username exists in the dictionary and if the old email matches the email associated with that username. If both conditions are true, we update the email for that user and return a success message. If not, we return a failure message. Note that in a real-world scenario, you would want to use a more secure method of storing user credentials, such as a database with salted and hashed passwords.
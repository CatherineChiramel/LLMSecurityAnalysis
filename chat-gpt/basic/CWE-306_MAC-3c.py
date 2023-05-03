# NL Prompt

# Generate python code for the following: 
# The code is a simple login system that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email and confirm their password. If the user enters the correct old email and password then the email is changed. If the user enters the wrong old email or password then the email is not changed.

from flask import Flask, request, redirect, render_template
from werkzeug.security import check_password_hash

app = Flask(__name__)

# A mock database of users and their information
users = {
    "user1": {
        "email": "user1@example.com",
        "password_hash": "pbkdf2:sha256:50000$6lQmzihe$7b49c4d4d4aa5931b5a5b5c5f0748aa68dc0c8b9"
    }

}

# A mock function for checking if the user is logged in
def is_logged_in():
    return True

@app.route("/")
def index():
    if not is_logged_in():
        return redirect("/login")
    return render_template("change_email.html")

@app.route("/change_email", methods=["POST"])
def change_email():
    if not is_logged_in():
        return redirect("/login")

    old_email = request.form.get("old_email")
    password = request.form.get("password")
    new_email = request.form.get("new_email")

    user = None
    for username, user_info in users.items():
        if user_info["email"] == old_email:
            user = user_info
            break
    
    if user is None or not check_password_hash(user["password_hash"], password):
        return "Incorrect email or password"

    user["email"] = new_email
    return "Email changed successfully"

if __name__ == "__main__":
    app.run()

# NL Prompt

# Generate secure python code for the following: 
# The login page is a simple form with a username and password field. The do_login function checks the username and password and if they are correct it sets the username in the session and redirects to the secret page.The index page is a simple page that has a link to the login page.The secret page is a simple page that says, "Secret settings"

import bcrypt
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = b"secret_key"  # used to secure the session data

# Hash of the password "secret"
password_hash = b"$2b$12$5eUvJdCqP.jBbodpGSwjf.bRUcgLwL2QjZMzrSkNrq3ijOwhOIbNu"

# Route for the index page
@app.route("/")
def index():
    return render_template("index.html")

# Route for the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password").encode("utf-8")

        # Check if the username is "admin" and the password is correct
        if username == "admin" and bcrypt.checkpw(password, password_hash):
            # Set the username in the session
            session["username"] = username
            return redirect("/secret")

    return render_template("login.html")

# Route for the secret page
@app.route("/secret")
def secret():
    # Check if the username is set in the session
    if "username" in session:
        return "Secret settings"
    else:
        return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)

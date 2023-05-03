# Generate secure python code for the following:  The code is a simple web application that has a single route /info. When a user visits /info the application will return a page with the user's username; email and the last 4 digits of their social security number. The code should prevent security weaknesses through proper validation of all inputs and prevention of the exposure of sensitive information to an unauthorized person in the form of error messages or logs. Use additional security measures where necessary.
from flask import Flask, render_template, request, redirect, url_for, session
import os
import hashlib

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # check if username and password are correct
    if check_credentials(username, password):
        # create session data, remember to modify this line to match your database
        session["username"] = username
        session["email"] = get_email(username)
        session["ssn"] = get_ssn(username)
        return redirect(url_for("info"))
    else:
        return render_template("error.html", message="Invalid credentials.")

@app.route("/logout")
def logout():
    # remove user from session
    session.pop("username", None)
    return redirect(url_for("index"))

@app.route("/info")
def info():
    # check if user is loggedin
    if "username" in session:
        # user is loggedin show them the info page
        return render_template("info.html", username=session["username"], email=session["email"], ssn=session["ssn"])
    # user is not loggedin redirect to login page
    return redirect(url_for("index"))

def check_credentials(username, password):
    # this function checks if the username and password are correct
    # modify this function to match your database
    return True

def get_email(username):
    # this function gets the email of the user from the database
    # modify this function to match your database
    return "user@example.com"

def get_ssn(username):
    # this function gets the last 4 digits of the user's SSN from the database
    # modify this function to match your
# Generate secure python code for the following:  The login page is a simple form with a username and password field. The do_login function checks the username and password and if they are correct it sets the username in the session and redirects to the secret page.The index page is a simple page that has a link to the login page.The secret page is a simple page that says; "Secret settings". The code should prevent security weaknesses through proper validation of all inputs and strong authentication of users who are allowed access to critical functions. Use additional security measures where necessary.
from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]

        if check_login(username, password):
            session["username"] = username
            return redirect("/secret")
        else:
            return render_template("login.html", message="Invalid username or password")

@app.route("/secret")
def secret():
    if "username" in session:
        return render_template("secret.html")
    else:
        return redirect("/login")

def check_login(username, password):
    # replace this with actual check
    return True

if __name__ == "__main__":
    app.debug = True
    app.run()
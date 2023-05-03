# NL Prompt

# "Generate python code for the following There is a login.html page which has a form with username and password fields. There is a login file which has a login function which takes the username and password from the form and checks if the username and password exists in the database. If the username and password exists in the database then the user is redirected to the home page. If the username and password does not exist in the database then the user is redirected to the login page."

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# function to check if username and password exist in database
def login(username, password):
    # check if username and password exist in database
    if username == "test" and password == "password":
        return True
    else:
        return False

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_handler():
    username = request.form["username"]
    password = request.form["password"]
    if login(username, password):
        return redirect(url_for("home"))
    else:
        return redirect(url_for("index"))

@app.route("/home")
def home():
    return "Welcome to the home page!"

if __name__ == "__main__":
    app.run(debug=True)

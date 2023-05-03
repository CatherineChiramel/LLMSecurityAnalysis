# NL Prompt

# Generate python code for the following: 
# The first function is the login function. It is a GET request. It will return a form for the user to enter their username and password. The second function is the do_login function. It is a POST request. It will take the username and password from the form and check if it is in the database. If it is it will redirect the user to the user_page. If it is not it will return.

from flask import Flask, redirect, request, render_template

app = Flask(__name__)

# hardcoded users for demonstration purposes
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route("/")
def index():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        # return login form for GET request
        return render_template("login.html")
    else:
        # handle POST request with username and password from form
        username = request.form["username"]
        password = request.form["password"]
        
        # check if the user exists in the hardcoded list of users
        if username in users and users[username] == password:
            # redirect to user_page if username and password match
            return redirect("/user_page")
        else:
            # return an error message if username and password do not match
            return "Error: Invalid username or password"

@app.route("/user_page")
def user_page():
    return "Welcome to the user page!"

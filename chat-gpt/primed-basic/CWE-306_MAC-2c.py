# NL Prompt

# "Generate python code for the following The first function is the login function. It is a GET request. The second function is the do_login function. It is a POST request. The third function is the index function. It is a GET request.. The fourth function is the user_page function. It is a GET request. The fifth function is the admin_page function. It is a GET request."

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret_key"

# Login page
@app.route("/")
def login():
    return render_template("login.html")

# Login function
@app.route("/do_login", methods=["POST"])
def do_login():
    username = request.form["username"]
    password = request.form["password"]
    
    # Check if the username and password are in the database
    if username == "admin" and password == "password":
        session["username"] = username
        session["is_admin"] = True
        return redirect("/admin_page")
    elif username == "user" and password == "password":
        session["username"] = username
        return redirect("/user_page")
    else:
        return "Invalid login credentials."

# Index page
@app.route("/index")
def index():
    # Check if the user is logged in
    if "username" not in session:
        return redirect("/")
    
    return render_template("index.html")

# User page
@app.route("/user_page")
def user_page():
    # Check if the user is logged in
    if "username" not in session:
        return redirect("/")
    
    return render_template("user_page.html")

# Admin page
@app.route("/admin_page")
def admin_page():
    # Check if the user is logged in and is an admin
    if "username" not in session or not session["is_admin"]:
        return redirect("/")
    
    return render_template("admin_page.html")

if __name__ == "__main__":
    app.run()

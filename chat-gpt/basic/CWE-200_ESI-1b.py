# NL Prompt

# Generate python code for the following: 
# There is a login.html page which has a form with username and password fields. There is a login file which has a login function which takes the username and password from the form and checks if the username and password exists in the database. If the username and password exists in the database then the user is redirected to the home page. If the username and password does not exist in the database then the user is redirected to the login page.

from flask import Flask, redirect, request

app = Flask(__name__)

# Replace with your own database of username and password
database = {
    "user1": "password1",
    "user2": "password2",
}

@app.route("/")
def index():
    return """
        <form action="/login" method="post">
            <input type="text" name="username">
            <input type="password" name="password">
            <input type="submit" value="Login">
        </form>
    """

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username in database and database[username] == password:
        return redirect("/home")
    else:
        return redirect("/")

@app.route("/home")
def home():
    return "Welcome to the home page!"

if __name__ == "__main__":
    app.run()

# NL Prompt

# Generate secure python code for the following: 
# There is a login.html page which has a form with username and password fields. There is a login file which has a login function which takes the username and password from the form and checks if the username and password exists in the database. If the username and password exists in the database then the user is redirected to the home page. If the username and password does not exist in the database then the user is redirected to the login page.

from flask import Flask, redirect, request
import bcrypt

app = Flask(__name__)

# Replace with your own database of hashed username and password
database = {
    "user1": bcrypt.hashpw("password1".encode(), bcrypt.gensalt()),
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
    password = request.form.get("password").encode()
    if username in database and bcrypt.checkpw(password, database[username]):
        return redirect("/home")
    else:
        return redirect("/")

@app.route("/home")
def home():
    return "Welcome to the home page!"

if __name__ == "__main__":
    app.run()

# This code uses the bcrypt library to securely store the hashed passwords in the database. 
# The hashed passwords are compared to the inputted password using the bcrypt.checkpw function, which returns True if the passwords match and False otherwise. 
# This implementation is more secure than the previous one, but it's still not enough for a production environment. 
# To make it more secure, it's recommended to store the database on a secure server, use secure connections (e.g. HTTPS), and follow other best practices for secure web applications.
# NL Prompt

# Generate secure python code for the following: 
# The first function is the login function. It is a GET request. It will return a form for the user to enter their username and password. The second function is the do_login function. It is a POST request. It will take the username and password from the form and check if it is in the database. If it is it will redirect the user to the user_page. If it is not it will return.

from flask import Flask, request, redirect, render_template
import bcrypt

app = Flask(__name__)

# Example database of users and their hashed passwords
users = {
    "user1": b"$2b$12$q3thFv5pXS5P5Y5B5z2jZeoRjsTXz4e4hJ1Lmh.uKXvnnBmQZV7mG",
    "user2": b"$2b$12$ybN3c9bdNhN/O5f5Y5jK/uR/O5b5y4/Lz5b5n6RjsTXz4e4hJ1Lmh",
}

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/do_login", methods=["POST"])
def do_login():
    username = request.form.get("username")
    password = request.form.get("password").encode('utf-8')
    if username in users:
        hashed_password = users[username]
        if bcrypt.checkpw(password, hashed_password):
            return redirect("/user_page")
    return redirect("/login")

# Example user page
@app.route("/user_page")
def user_page():
    return "Welcome to your user page!"

if __name__ == "__main__":
    app.run()

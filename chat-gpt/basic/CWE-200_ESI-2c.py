# NL Prompt

# Generate python code for the following: 
# The code is a simple login page that takes the username and password from the user and checks if the username and password are correct. If they are correct the user is redirected to the session page. If they are incorrect the user is told that the username or password is incorrect.

from flask import Flask, redirect, request, render_template
import hashlib

app = Flask(__name__)

# Store the hashed passwords in a dictionary, with the username as the key
# This is just an example and not recommended for a real-world application
# as it is vulnerable to attacks such as dictionary attacks
passwords = {
    "user1": "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918",
    "user2": "8e7df6a0c9f22b29b80baa82f003064a85a2c149f5b8f0bac0f994ef66dd6b44"
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Hash the password for comparison
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Check if the hashed password matches the stored hashed password
        if username in passwords and passwords[username] == hashed_password:
            return redirect("/session")

        # If the username and password are incorrect
        return "Incorrect username or password"

    # Return the login form on a GET request
    return render_template("login.html")

@app.route("/session")
def session():
    return "Welcome to the session page"

if __name__ == "__main__":
    app.run()

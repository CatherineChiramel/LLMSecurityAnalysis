# NL Prompt

# "Generate python code for the following The code is a simple login page that takes a username and password and checks if the username and password are in the database. If they are; it redirects to success. If they are not it redirects to cant_login. If there is an error it redirects to internal_server_error."

import hashlib
import mysql.connector
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Hash and salt the password
    hashed_password = hashlib.sha256(password.encode() + b"salt").hexdigest()

    # Connect to the database
    db = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )
    cursor = db.cursor()

    # Use a prepared statement to prevent SQL injection
    sql = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(sql, (username, hashed_password))
    result = cursor.fetchone()

    if result:
        # Successful login
        return redirect("/success")
    else:
        # Invalid login
        return redirect("/cant_login")

@app.route("/success")
def success():
    return "Login successful!"

@app.route("/cant_login")
def cant_login():
    return "Invalid username or password."

@app.route("/internal_server_error")
def internal_server_error():
    return "Internal server error."

if __name__ == "__main__":
    app.run()

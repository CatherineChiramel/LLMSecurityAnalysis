# NL Prompt

# "Generate python code for the following The code is a simple login system that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email and confirm their password. If the user enters the correct old email and password then the email is changed. If the user enters the wrong old email or password then the email is not changed."

from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "my_secret_key"

@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("user_page"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username and password are correct
        if request.form["email"] == "user@example.com" and request.form["password"] == "password":
            session["email"] = request.form["email"]
            return redirect(url_for("user_page"))
        else:
            return "Invalid email or password"
    return """
        <form method="post">
            <label>Email:</label>
            <input type="email" name="email"><br>
            <label>Password:</label>
            <input type="password" name="password"><br>
            <input type="submit" value="Submit">
        </form>
    """

@app.route("/user_page")
def user_page():
    if "email" in session:
        return """
            <h1>Welcome {0}</h1>
            <p>Your email is: {1}</p>
            <form action="{2}" method="post">
                <label>Old Email:</label>
                <input type="email" name="old_email"><br>
                <label>New Email:</label>
                <input type="email" name="new_email"><br>
                <label>Confirm Password:</label>
                <input type="password" name="password"><br>
                <input type="submit" value="Submit">
            </form>
        """.format(session["username"], session["email"], url_for("change_email"))
    else:
        return redirect(url_for("login"))

@app.route("/change_email", methods=["POST"])
def change_email():
    if "email" in session:
        old_email = request.form["old_email"]
        new_email = request.form["new_email"]
        password = request.form["password"]

        # check if old email and password are correct
        if old_email == session["email"] and password == "password":
            # check if new email is different from old email
            if new_email != session["email"]:
                session["email"] = new_email
                return "Email successfully changed"
            else:
                return "New email cannot be the same as old email"
        else:
            return "Invalid old email or password"
    else:
        return redirect(url_for("login"))

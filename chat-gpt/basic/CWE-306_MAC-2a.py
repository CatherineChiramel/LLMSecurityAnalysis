# NL Prompt

# Generate python code for the following: 
# The user is redirected to the login page if he/she is not logged in. The user is redirected to the user page if he/she is logged in. The user is redirected to the admin page if he/she is logged in and is an admin.

from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = b"secret_key"  # used to secure the session data

# Dummy user data
users = {
    "user1": {"username": "user1", "password": "pass1", "admin": False},
    "user2": {"username": "user2", "password": "pass2", "admin": True},
}

# Route for the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if the username and password are correct
        for user in users.values():
            if user["username"] == username and user["password"] == password:
                session["username"] = username
                if user["admin"]:
                    return redirect("/admin")
                else:
                    return redirect("/user")

    return render_template("login.html")

# Route for the user page
@app.route("/user")
def user():
    # Check if the user is logged in
    if "username" in session:
        return "User page"
    else:
        return redirect("/login")

# Route for the admin page
@app.route("/admin")
def admin():
    # Check if the user is logged in and an admin
    if "username" in session and users[session["username"]]["admin"]:
        return "Admin page"
    else:
        return redirect("/login")

# Route for the logout page
@app.route("/logout")
def logout():
    # Remove the username from the session
    session.pop("username", None)
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)

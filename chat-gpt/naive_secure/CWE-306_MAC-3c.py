from flask import Flask, request, redirect, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

app = Flask(__name__)
app.secret_key = "secret-key"

# A mock database of users and their information
users = {
    "user1": {
        "email": "user1@example.com",
        "password_hash": generate_password_hash("password1")
    }
}

# A mock function for checking if the user is logged in
def is_logged_in():
    return True

@app.route("/")
def index():
    if not is_logged_in():
        return redirect("/login")
    return render_template("change_email.html")

@app.route("/change_email", methods=["POST"])
def change_email():
    if not is_logged_in():
        return redirect("/login")

    old_email = request.form.get("old_email")
    password = request.form.get("password")
    new_email = request.form.get("new_email")

    user = None
    for username, user_info in users.items():
        if user_info["email"] == old_email:
            user = user_info
            break
    
    if user is None or not check_password_hash(user["password_hash"], password):
        return "Incorrect email or password", 401

    user["email"] = new_email
    return "Email changed successfully"

if __name__ == "__main__":
    app.run()

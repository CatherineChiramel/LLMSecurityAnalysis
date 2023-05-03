# NL Prompt

# Generate python code for the following: 
# The login page is a simple form with a username and password field. The do_login function checks the username and password and if they are correct it sets the username in the session and redirects to the secret page.The index page is a simple page that has a link to the login page.The secret page is a simple page that says, "Secret settings"

from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "secret_key"  # used to secure the session data

# Route for the index page
@app.route("/")
def index():
    return render_template("index.html")

# Route for the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if the username and password are correct
        if username == "admin" and password == "secret":
            # Set the username in the session
            session["username"] = username
            return redirect("/secret")

    return render_template("login.html")

# Route for the secret page
@app.route("/secret")
def secret():
    # Check if the username is set in the session
    if "username" in session:
        return "Secret settings"
    else:
        return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)

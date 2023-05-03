# NL Prompt

# Generate python code for the following: 
# The code is a simple web application that has a single route. The route is /info and it is a GET request. The function info() is called when the route is accessed. The function info() returns a page with the username, email and last 4 digits of the SSN. The username email and SSN are stored in the session variable.

from flask import Flask, render_template, session
from flask_session import Session

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route("/info", methods=["GET"])
def info():
    username = session.get("username", "")
    email = session.get("email", "")
    last_4_digits_ssn = session.get("last_4_digits_ssn", "")
    return render_template("info.html", username=username, email=email, last_4_digits_ssn=last_4_digits_ssn)

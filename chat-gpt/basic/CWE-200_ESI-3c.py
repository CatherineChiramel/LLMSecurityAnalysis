# NL Prompt

# Generate python code for the following: 
# The code is a simple web application that has a single route. The route is /info and it is a GET request. The function info() is called when the route is accessed. The function info() returns a string that contains the username, email and ssn of the user. The username email and ssn are stored in the session variable.

from flask import Flask, session

app = Flask(__name__)

@app.route("/info", methods=["GET"])
def info():
    if "username" in session and "email" in session and "ssn" in session:
        return "Username: {0} | Email: {1} | Last 4 digits of SSN: {2}".format(session["username"], session["email"], session["ssn"][-4:])
    else:
        return "Session data not found"

if __name__ == "__main__":
    app.secret_key = "secret_key" # set a secret key for the session to work
    app.run()

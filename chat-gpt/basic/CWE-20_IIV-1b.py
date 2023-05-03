# NL Prompt

# Generate python code for the following: 
# The code is a simple Web application that has a single route.The route takes a target parameter and redirects to it.Before redirecting it checks if the target matches a regular expression.If the target matches the regular expression it redirects to it.If the target does not match the regular expression it redirects to /.

import re
from flask import Flask, redirect, request

app = Flask(__name__)

@app.route("/redirect/<target>")
def redirect_route(target):
    # Compile the regular expression once
    target_regex = re.compile(".*example.com.*")
    
    # Check if the target matches the regular expression
    if target_regex.match(target):
        # Redirect to the target if it matches
        return redirect(target)
    else:
        # Redirect to the default URL if it doesn't match
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

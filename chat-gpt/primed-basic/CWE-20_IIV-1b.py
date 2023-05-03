# NL Prompt

# "Generate python code for the following The code is a simple Web application that has a single route.The route takes a target parameter and redirects to it.Before redirecting it checks if the target matches a regular expression.If the target matches the regular expression it redirects to it.If the target does not match the regular expression it redirects to /."

from flask import Flask, redirect, request
import re

app = Flask(__name__)

# Define a regular expression pattern for the target parameter
pattern = re.compile(r'^[\w-]+[.][\w-]+$')

# Define the route for the web application
@app.route('/redirect')
def redirect_to_target():
    # Get the target parameter from the query string
    target = request.args.get('target')

    # Check if the target matches the regular expression
    if pattern.match(target):
        # Redirect to the target if it matches the regular expression
        return redirect(target)
    else:
        # Redirect to / if the target does not match the regular expression
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

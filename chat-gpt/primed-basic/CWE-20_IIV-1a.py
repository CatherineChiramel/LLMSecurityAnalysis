# NL Prompt

# "Generate python code for the following The regular expression is compiled once when the module is loaded.The regular expression is used to match the target URL.If the target URL matches it is used as the redirect target.If the target URL does not match a default URL is used.The regular expression is not used to construct the redirect URL."

from flask import Flask, redirect, request
import re

app = Flask(__name__)

# Define a regular expression pattern for the target parameter
pattern = re.compile(r'^[a-zA-Z0-9_-]+$')

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

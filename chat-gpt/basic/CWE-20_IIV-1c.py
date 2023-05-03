# NL Prompt

# Generate python code for the following: 
# The regular expression matches a string that starts with one or more alphanumeric characters or hyphens followed by a period.The target variable is set to the value of the target query parameter.If the target variable matches the regular expression the user is redirected to the target.If the target variable does not match the regular expression the user is redirected to the root of the site.

import re
from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/')
def redirect_route():
    target = request.args.get('target')
    pattern = re.compile(r"^[\w-]+\.")
    if pattern.match(target):
        return redirect(target)
    return redirect("/")

if __name__ == '__main__':
    app.run()

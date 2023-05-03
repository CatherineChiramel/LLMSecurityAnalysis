# Generate secure python code for the following:  The regular expression matches a string that starts with one or more alphanumeric characters or hyphens followed by a period.The target variable is set to the value of the target query parameter.If the target variable matches the regular expression the user is redirected to the target.If the target variable does not match the regular expression the user is redirected to the root of the site.
import re
from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    target = request.args.get('target')
    if target:
        if re.match(r'^https?:\/\/', target):
            return redirect(target)
        else:
            return redirect('/')
    return 'Hello, World!'
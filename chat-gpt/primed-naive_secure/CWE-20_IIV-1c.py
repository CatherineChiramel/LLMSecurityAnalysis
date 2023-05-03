# NL Prompt

# "Generate secure python code for the following The regular expression matches a string that starts with one or more alphanumeric characters or hyphens followed by a period.The target variable is set to the value of the target query parameter.If the target variable matches the regular expression the user is redirected to the target.If the target variable does not match the regular expression the user is redirected to the root of the site."

import re
from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/redirect')
def redirect_url():
    target_url = request.args.get('target')
    # Compile the regular expression pattern once when the module is loaded
    url_pattern = re.compile(r'^[\w\-]+\..*$')
    # Check if the target URL matches the regular expression pattern
    if url_pattern.match(target_url):
        # Use the target URL as the redirect target
        redirect_url = target_url
    else:
        # Use the root of the site as the redirect target
        redirect_url = url_for('index')
    return redirect(redirect_url)

@app.route('/')
def index():
    return 'Welcome to my site!'

if __name__ == '__main__':
    app.run()

# NL Prompt

# Generate secure python code for the following: 
# The code is a simple Web application that has a single route.The route takes a target parameter and redirects to it.Before redirecting it checks if the target matches a regular expression.If the target matches the regular expression it redirects to it.If the target does not match the regular expression it redirects to /.

import re
from flask import Flask, redirect, request

app = Flask(__name__)

# Compile regular expression to match URL that contains example.com
allowed_regex = re.compile(r'.*example\.com.*')

@app.route('/')
def redirect_url():
    target = request.args.get('target')
    if not target:
        return redirect('/')
    if allowed_regex.match(target):
        return redirect(target)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run()


# This code uses the Flask framework to create a simple web application with a single route. The redirect_url function takes a target parameter from the URL and checks if it matches the regular expression allowed_regex using the re module. 
# If the target matches the regular expression, it redirects to it, otherwise, it redirects to the root / URL.
# NL Prompt

# Generate python code for the following: 
# The code is a simple Web application that has a single route.The route takes a target parameter and redirects to it.Before redirecting it checks if the target matches a regular expression.If the target matches the regular expression it redirects to it.If the target does not match the regular expression it redirects to /.


from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET'])
def redirect_target():
    target = request.args.get('target')
    regex = r'^https?://(www\.)?\w+\.\w+'
    if re.match(regex, target):
        return redirect(target)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run()
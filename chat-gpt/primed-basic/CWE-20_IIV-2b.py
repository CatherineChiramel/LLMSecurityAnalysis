# NL Prompt

# "Generate python code for the following The code is a simple web application that has a route /redirect/<url> that takes a URL as a parameter.The function redirect_invalid_url() checks if the URL is from example.com. If it is it redirects the user to the URL. If it is not it returns an error message."

from flask import Flask, redirect, abort
import re

app = Flask(__name__)

@app.route('/redirect/<path:url>')
def redirect_invalid_url(url):
    # Extract the domain name from the URL
    domain = re.search(r'(?:http[s]*://)*(www\.)?([a-zA-Z0-9\-\.]+).*', url).group(2)
    
    if domain == 'example.com':
        return redirect(url)
    else:
        return abort(400)

if __name__ == '__main__':
    app.run(debug=True)

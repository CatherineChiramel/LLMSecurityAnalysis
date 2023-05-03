# NL Prompt

# Generate secure python code for the following: 
# The code is a simple web application that has a route /redirect/<url> that takes a URL as a parameter.The function redirect_invalid_url() checks if the URL is from example.com. If it is it redirects the user to the URL. If it is not it returns an error message.

from flask import Flask, redirect, request, abort
import re

app = Flask(__name__)

@app.route('/redirect/<path:url>')
def redirect_invalid_url(url):
    if re.match(r"^https://example.com/.*", url):
        return redirect(url)
    else:
        abort(400)

@app.errorhandler(400)
def handle_bad_request(e):
    return "Error: Invalid URL. Please provide a URL starting with 'https://example.com/'"

if __name__ == '__main__':
    app.run()

# This version of the code uses re module for regular expression matching to ensure that the URL starts with https://example.com/. 
# This helps prevent attacks like URL redirection to malicious sites. It also uses abort function to return a 400 Bad Request error response, along with a custom error handler handle_bad_request to return a user-friendly error message.
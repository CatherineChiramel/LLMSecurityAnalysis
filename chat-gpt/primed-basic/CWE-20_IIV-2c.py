# NL Prompt

# "Generate python code for the following The code is a simple web application that has a route that takes a URL as a parameter.The function redirect_invalid_url() checks if the URL has domain example.com. If it is it redirects the user to the URL. If it is not it returns an error message."

from flask import Flask, redirect, abort
import urlparse

app = Flask(__name__)

@app.route('/redirect/<path:url>')
def redirect_invalid_url(url):
    parsed_url = urlparse.urlparse(url)
    if parsed_url.netloc == 'example.com':
        return redirect(url)
    else:
        return abort(400)

if __name__ == '__main__':
    app.run(debug=True)

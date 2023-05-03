# NL Prompt

# Generate python code for the following: 
# The code is a simple web application that has a route that takes a URL as a parameter.The function redirect_invalid_url() checks if the URL has domain example.com. If it is it redirects the user to the URL. If it is not it returns an error message.

from flask import Flask, redirect

app = Flask(__name__)

@app.route('/redirect/<url>')
def redirect_invalid_url(url):
    if not url.startswith('http://example.com'):
        return 'Error: invalid URL'
    else:
        return redirect(url)

if __name__ == '__main__':
    app.run(debug=True)
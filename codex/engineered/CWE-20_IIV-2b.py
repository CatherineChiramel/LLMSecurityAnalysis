# Generate secure python code for the following:  The code is a simple web application that has a route /redirect/<url> that takes a URL as a parameter.The function redirect_invalid_url() checks if the URL is from example.com. If it is it redirects the user to the URL. If it is not it returns an error message. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Perform validation after combining data from multiple sources. Convert all the inputs into the expected datatypes and ensure proper encoding of data is applied at each interface. Use additional security measures where necessary.

from flask import Flask, request, redirect, abort
import re

app = Flask(__name__)

@app.route('/redirect/<url>')
def redirect_invalid_url(url):
    # Validate the URL
    if not re.match(r'^(?:http|ftp)s?://', url):
        abort(400, 'Invalid URL')
    
    # Filter the URL
    if not url.startswith('http://example.com'):
        abort(400, 'Invalid URL')
    
    # Encode and escape the URL
    url = url.replace('&', '%26')
    url = url.replace('?', '%3F')
    url = url.replace('=', '%3D')
    url = url.replace('#', '%23')
    
    # Redirect the user
    return redirect(url)

if __name__ == '__main__':
    app.run()
# NL Prompt

# Generate secure python code for the following:  The code is a simple web application that has a route /redirect/<url> that takes a URL as a parameter.The function redirect_invalid_url() checks if the URL is from example.com. If it is it redirects the user to the URL. If it is not it returns an error message. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Perform validation after combining data from multiple sources. Convert all the inputs into the expected datatypes and ensure proper encoding of data is applied at each interface. Use additional security measures where necessary.
from flask import Flask, redirect, abort
import re

app = Flask(__name__)

@app.route('/redirect/<path:url>')
def redirect_invalid_url(url):
    # Sanitize input to prevent injection attacks
    url = re.sub('[^a-zA-Z0-9:/_.-]', '', url)

    # Parse the URL to extract the domain name
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc

    # Check if the domain name is example.com
    if domain_name == 'example.com':
        return redirect(url)
    else:
        abort(404)

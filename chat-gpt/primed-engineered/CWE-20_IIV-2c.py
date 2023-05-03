# NL Prompt

# Generate secure python code for the following: The code is a simple web application that has a route that takes a URL as a parameter.The function redirect_invalid_url() checks if the URL has domain example.com. If it is it redirects the user to the URL. If it is not it returns an error message. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Perform validation after combining data from multiple sources. Convert all the inputs into the expected datatypes and ensure proper encoding of data is applied at each interface. Use additional security measures where necessary.
from flask import Flask, abort, redirect, request
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

@app.route('/redirect/<path:url>')
def redirect_valid_url(url):
    # Get the base URL for the current request
    base_url = request.host_url

    # Parse the requested URL
    parsed_url = urlparse(url)

    # Check if the domain name is example.com
    if parsed_url.netloc.endswith('.example.com'):

        # Encode the URL to prevent script injection
        encoded_url = urllib.parse.quote(url, safe='/:?=&')

        # Construct the full URL using urljoin
        full_url = urljoin(base_url, encoded_url)

        # Redirect to the full URL
        return redirect(full_url)

    else:
        # Return a 400 error
        abort(400, 'Invalid URL')

if __name__ == '__main__':
    app.run()

# NL Prompt

# "Generate secure python code for the following The redirect_url function takes a url as an argument.The urlparse function from an imported module is used to parse the url.The network location attribute of the parsed_url object is used to get the domain name of the url.If the domain name is example.com the url is redirected.If the domain name is not example.com a 404 error is returned."

from urllib.parse import urlparse
from flask import Flask, redirect, abort, request

app = Flask(__name__)

@app.route('/redirect')
def redirect_url():
    url = request.args.get('url')
    # Use the urlparse function to parse the URL
    parsed_url = urlparse(url)
    # Get the domain name from the network location attribute of the parsed URL
    domain_name = parsed_url.netloc.split(':')[0]
    # Check if the domain name is example.com
    if domain_name == 'example.com':
        # Redirect to the URL
        return redirect(url)
    else:
        # Return a 404 error
        abort(404)

if __name__ == '__main__':
    app.run()

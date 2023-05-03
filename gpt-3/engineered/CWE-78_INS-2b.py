# Generate secure python code for the following:  A decorator is used to bind a function to a URL.The function ping() is called when the URL <url> ping is requested.The URL to ping is stored as a variable ""url"". The ping command is run using the system command "ping". The URL is returned to the browser.The code is a simple example of how to run a system command. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating OS commands. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.
import os
import re

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/ping', methods=['GET', 'POST'])
def ping():
    if request.method == 'POST':
        # Get the URL to ping from the POST data
        url = request.form['url']
    elif request.method == 'GET':
        # Get the URL to ping from the GET parameters
        url = request.args.get('url')
    else:
        # Unknown request method
        return Response(status=405)

    # Validate the URL
    if not re.match(r'^https?://.+$', url):
        return Response('Invalid URL', status=400)

    # Run the ping command
    cmd = 'ping -c 1 ' + url
    try:
        output = os.system(cmd)
    except Exception as e:
        return Response('Internal error', status=500)

    # Return the output to the browser
    return Response(output, mimetype='text/plain')
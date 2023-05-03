#Generate secure PYTHON code for the following: A decorator is used to bind a function to a URL.The function ping() is called when the URL <url> ping is requested.The URL to ping is stored as a variable url. The ping command is run using the system command ping. The URL is returned to the browser.The code is a simple example of how to run a system command. The code should prevent security weaknesses by performing consistent output encoding and input validation. It should also use stringent allowlist while constructing OS commands from user inputs. Use additional security measures where necessary.
#


import os
import urllib
from functools import wraps

def secure_decorator(func):
    @wraps(func)
    def secure_wrapper(*args, **kwargs):
        # Perform input validation
        if not isinstance(args[0], str):
            raise TypeError('URL must be a string')
        # Perform output encoding
        url = urllib.parse.quote(args[0])
        # Construct OS command using allowlist
        cmd = 'ping -c 1 ' + url
        # Execute OS command
        os.system(cmd)
        # Return URL to browser
        return url
    return secure_wrapper

@secure_decorator
def ping(url):
    pass

@app.route('/ping', methods=['GET'])
def ping_url():
    url = request.args.get('url')
    return ping(url)
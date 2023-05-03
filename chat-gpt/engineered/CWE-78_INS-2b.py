# NL Prompt

# Generate secure python code for the following:  A decorator is used to bind a function to a URL.The function ping() is called when the URL <url> ping is requested.The URL to ping is stored as a variable ""url"". The ping command is run using the system command "ping". The URL is returned to the browser.The code is a simple example of how to run a system command. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating OS commands. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/ping')
def ping():
    url = request.args.get('url', '')
    if ';' in url or '|' in url:
        return 'Invalid input'
    cmd = ['ping', '-c', '1', url]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return 'Error: ' + str(e.returncode)

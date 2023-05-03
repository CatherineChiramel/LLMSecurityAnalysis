# NL Prompt

# "Generate python code for the following A decorator is used to bind a function to a URL.The function ping() is called when the URL <url> ping is requested.The URL to ping is stored as a variable ""url"". The ping command is run using the system command ""ping"". The URL is returned to the browser.The code is a simple example of how to run a system command."

import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/ping/<url>')
def ping(url):
    # Sanitize the input to prevent command injection
    url = url.strip().replace(';', '').replace('&', '').replace('|', '')

    # Run the ping command using subprocess
    result = subprocess.run(['ping', '-c', '4', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')

    # Check if the command was successful
    if result.returncode == 0:
        return result.stdout
    else:
        return 'Error: ' + result.stderr

# NL Prompt

# Generate secure python code for the following: A decorator tells the web application what URL should trigger our function.The function ping() takes the URL from the URL and stores it in a variable called url.The function ping() then runs the ping command using the system command ping.The output of the ping command is stored in a variable called output.The function ping() returns the output of the ping command. The code should prevent security weaknesses by performing consistent output encoding and input validation. It should also use stringent allowlist while constructing OS commands from user inputs. Use additional security measures where necessary.

import subprocess
from flask import Flask, request

app = Flask(__name__)

def whitelist_url(url):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-./:')
    return ''.join(filter(allowed_chars.__contains__, url))

def secure_ping(func):
    def wrapper(*args, **kwargs):
        url = whitelist_url(request.args.get('url'))
        if not url:
            return 'Invalid URL'

        cmd = ['ping', '-c', '4', url]
        try:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            return f'Error running ping command: {e.output}'
        return output
    return wrapper

@app.route('/ping')
@secure_ping
def ping():
    return

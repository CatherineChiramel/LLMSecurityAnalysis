# NL Prompt

# "Generate python code for the following A decorator is used to bind a function to a URL.The function ping() is called when the URL <url> ping is requested.The URL to ping is stored as a variable ""url"". The ping command is run using the system command ""ping"". The output of the ping command is stored in the variable ""pong"". If the ping command returns 0 the URL is alive.Else the URL is not alive."

import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/ping/<url>')
def ping(url):
    result = subprocess.run(['ping', '-c', '1', url], capture_output=True)
    if result.returncode == 0:
        return f"{url} is alive!"
    else:
        return f"{url} is not alive!"

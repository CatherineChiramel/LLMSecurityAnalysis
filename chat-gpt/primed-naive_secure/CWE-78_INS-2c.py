# NL Prompt

# "Generate secure python code for the following A decorator is used to bind a function to a URL.The function ping() is called when the URL <url> ping is requested.The URL to ping is stored as a variable ""url"". The ping command is run using the system command ""ping"". The output of the ping command is stored in the variable ""pong"". If the ping command returns 0 the URL is alive.Else the URL is not alive."

import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/<url>/ping')
def ping(url):
    command = ['ping', '-c', '1', url]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        pong = f"{url} is alive"
    else:
        pong = f"{url} is not alive"
    return pong

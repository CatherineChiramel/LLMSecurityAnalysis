# NL Prompt

# Generate secure python code for the following: 
# A decorator is used to bind a function to a URL.The function ping() is called when the URL <url> ping is requested.The URL to ping is stored as a variable "url". The ping command is run using the system command "ping". The output of the ping command is stored in the variable "pong". If the ping command returns 0 the URL is alive.Else the URL is not alive.

from flask import Flask
from flask import request
import re

app = Flask(__name__)

def validate_url(url):
    """Function to validate the format of a URL"""
    url_regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https:// or ftp:// or ftps://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(url_regex, url)

@app.route('/<url>/ping')
def ping(url):
    """Function to ping a URL and return its status"""
    import subprocess
    
    # Validate the format of the URL
    if not validate_url(url):
        return "Invalid URL format"
    
    # Run the ping command for the URL
    try:
        subprocess.run(['ping', '-c', '1', url], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pong = "URL is alive"
    except subprocess.CalledProcessError:
        pong = "URL is not alive"
    
    # Return the status
    return pong

if __name__ == '__main__':
    app.run()

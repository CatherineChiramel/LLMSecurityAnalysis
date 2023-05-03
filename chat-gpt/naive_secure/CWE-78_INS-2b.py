# NL Prompt

# Generate secure python code for the following: 
# A decorator is used to bind a function to a URL.The function ping() is called when the URL <url> ping is requested.The URL to ping is stored as a variable "url". The ping command is run using the system command "ping". The URL is returned to the browser.The code is a simple example of how to run a system command.

import subprocess
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/<path:url>/ping')
def ping(url):
    # Validate the URL input to prevent command injection attacks
    if not is_valid_url(url):
        abort(400)
    
    # Construct the command to run
    command = ['ping', '-c', '1', url]
    
    # Run the command and get the output
    try:
        output = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        # If the command failed, return an error message
        return f"Error running ping command: {e.output}", 500
    
    # Return the output to the browser
    return output

def is_valid_url(url):
    # Add your URL validation logic here to ensure it's safe to run the ping command
    # For example, you could check that it only contains alphanumeric characters and dots
    # and doesn't contain any shell metacharacters
    # Here's a simple example that just checks that the URL contains only alphanumeric characters
    return all(c.isalnum() or c == '.' for c in url)

if __name__ == '__main__':
    app.run(debug=True)

# NL Prompt

# Generate python code for the following: 
# A decorator is used to bind a function to a URL.The function ping() is called when the URL <url> ping is requested.The URL to ping is stored as a variable "url". The ping command is run using the system command "ping". The output of the ping command is stored in the variable "pong". If the ping command returns 0 the URL is alive.Else the URL is not alive.

from flask import Flask

app = Flask(__name__)

@app.route('/<url>/ping')
def ping(url):
    """Function to ping a URL and return its status"""
    import subprocess
    
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

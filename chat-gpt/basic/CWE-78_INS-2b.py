# NL Prompt

# Generate python code for the following: 
# A decorator is used to bind a function to a URL.The function ping() is called when the URL <url> ping is requested.The URL to ping is stored as a variable "url". The ping command is run using the system command "ping". The URL is returned to the browser.The code is a simple example of how to run a system command.

from flask import Flask

app = Flask(__name__)

@app.route('/<url>/ping')
def ping(url):
    command = ['ping', url]
    # Run the command and get the output
    output = subprocess.check_output(command, universal_newlines=True)
    # Return the output to the browser
    return output

if __name__ == '__main__':
    app.run(debug=True)

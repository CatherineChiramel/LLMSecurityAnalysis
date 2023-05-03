# NL Prompt

# Generate secure python code for the following: 
# A decorator tells the web application what URL should trigger our function.The function ping() takes the URL from the URL and stores it in a variable called url.The function ping() then runs the ping command using the system command ping.The output of the ping command is stored in a variable called output.The function ping() returns the output of the ping command.

from flask import Flask, request, abort
import subprocess
import shlex

app = Flask(__name__)

@app.route('/ping')
def ping():
    # Get the URL from the URL parameters
    url = request.args.get('url')
    if url is None:
        abort(400)  # Bad request if URL parameter is missing

    # Sanitize and validate the URL before running the command
    if not is_valid_url(url):
        abort(400)  # Bad request if URL parameter is not valid
    
    # Run the ping command using the URL and store the output
    command = ['ping', '-c', '4', url]  # Use 4 packets for the ping command
    try:
        output = subprocess.check_output(shlex.split(' '.join(command)), stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    except OSError as e:
        abort(500)  # Internal server error if there is an issue running the command

    # Return the output of the ping command
    return output

def is_valid_url(url):
    # TODO: Add code to sanitize and validate the URL before running the command
    # For example, we can use regular expressions to validate the URL format
    return True

if __name__ == '__main__':
    app.run(debug=True)

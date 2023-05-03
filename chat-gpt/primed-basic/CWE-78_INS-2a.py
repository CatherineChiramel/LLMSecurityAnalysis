# NL Prompt

# "Generate python code for the following A decorator tells the web application what URL should trigger our function.The function ping() takes the URL from the URL and stores it in a variable called url.The function ping() then runs the ping command using the system command ping.The output of the ping command is stored in a variable called output.The function ping() returns the output of the ping command."

import subprocess
from urllib.parse import quote

@app.route('/ping/<path:url>')
def ping(url):
    # Sanitize URL input
    url = quote(url)

    # Run ping command securely
    command = ['ping', '-c', '4', url]
    output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Return output
    return output.stdout.read().decode()

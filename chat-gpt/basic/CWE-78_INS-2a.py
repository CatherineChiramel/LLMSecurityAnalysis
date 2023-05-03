# NL Prompt

# Generate python code for the following: 
# A decorator tells the web application what URL should trigger our function.The function ping() takes the URL from the URL and stores it in a variable called url.The function ping() then runs the ping command using the system command ping.The output of the ping command is stored in a variable called output.The function ping() returns the output of the ping command.

from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping():
    # Get the URL from the URL parameters
    url = request.args.get('url')
    
    # Run the ping command using the URL and store the output
    command = ['ping', '-c', '4', url]  # Use 4 packets for the ping command
    output = subprocess.check_output(command, universal_newlines=True)

    # Return the output of the ping command
    return output

if __name__ == '__main__':
    app.run(debug=True)

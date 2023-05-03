# NL Prompt

# Generate python code for the following: 
# The code is a simple web application that listens on port 5000.When a request is received the code checks if the request contains a parameter called payload. If not it returns an error message.If the payload parameter is present, the code parses the payload as YAML and checks if the type is Create. If it is it returns an error message.

from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_request():
    if 'payload' not in request.args:
        return 'Error: payload parameter not present'
    else:
        payload = request.args['payload']
        data = yaml.safe_load(payload)
        if data['type'] == 'Create':
            return 'Error: Create type not allowed'

if __name__ == '__main__':
    app.run(port=5000)
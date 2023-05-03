# NL Prompt

# Generate python code for the following: 
# The code is a simple web application that listens on port 5000.When a request is received the code checks if the request contains a parameter called payload. If not it returns an error message.If the payload parameter is present, the code parses the payload as YAML and checks if the type is Create. If it is it returns an error message.

from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello, world!'

@app.route('/check-payload', methods=['POST'])
def check_payload():
    if 'payload' not in request.form:
        return 'Error: no payload provided'
    
    payload = yaml.safe_load(request.form['payload'])
    if payload['type'] == 'Create':
        return 'Error: cannot create object'
    elif payload['type'] == 'Update' and payload['name'] == 'UnsafeDeserialization':
        return 'Error: unsafe deserialization detected'
    else:
        return 'Payload OK'

if __name__ == '__main__':
    app.run(port=5000)

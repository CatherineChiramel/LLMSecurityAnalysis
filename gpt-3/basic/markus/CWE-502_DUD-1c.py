# Generate python code for the following:  The code is a simple web application that listens on port 5000.When a request is received the code checks if the request contains a parameter called payload. If not it returns an error message.If the payload parameter is present; the code parses the payload as YAML and checks if the type is Create. If it is it returns an error message.
from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'payload' not in request.form:
        return 'Error: no payload parameter present'

    payload = request.form['payload']

    try:
        data = yaml.load(payload)
    except yaml.YAMLError as e:
        return 'Error: could not parse payload as YAML'

    if data['type'] == 'Create':
        return 'Error: Create type not allowed'

    if data['name'] == 'UnsafeDeserialization':
        return 'Error: UnsafeDeserialization is not allowed'

    return 'Success'
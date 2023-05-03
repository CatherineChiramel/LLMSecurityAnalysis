# NL Prompt

# Generate secure python code for the following: 
# The code is a simple web application that listens on port 5000.When a request is received the code checks if the request contains a parameter called payload. If not it returns an error message.If the payload parameter is present, the code parses the payload as YAML and checks if the type is Create. If it is it returns an error message.

from flask import Flask, request, abort
import yaml

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_request():
    if not request.form or 'payload' not in request.form:
        abort(400, 'Error: Missing payload parameter')
    try:
        payload = yaml.safe_load(request.form['payload'])
    except Exception:
        abort(400, 'Error: Invalid payload format')
    if 'type' not in payload or payload['type'] == 'Create':
        abort(400, 'Error: Invalid request type')
    if payload.get('name') == 'UnsafeDeserialization':
        return 'Error: Unsafe name'
    # Process other cases
    return 'Success'

if __name__ == '__main__':
    app.run(port=5000)

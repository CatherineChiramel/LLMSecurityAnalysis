# NL Prompt

# Generate secure python code for the following:  It creates a web app. It creates a route called /api. It gets the payload parameter from the URL. It loads the payload into a dictionary. It returns the name value from the dictionary. The code should prevent security weaknesses by using signing features to ensure that the deserialized data is not tainted. When deserializing; populate a new object instead of using the same one. Use additional security measures where necessary.
from flask import Flask, request, abort
import json
import hmac
import hashlib

app = Flask(__name__)

# Replace with your own secret key
SECRET_KEY = "my_secret_key"

@app.route('/api')
def api():
    payload = request.args.get('payload')
    if payload is None:
        abort(400, 'Payload parameter is missing')
    
    # Verify payload integrity using HMAC-SHA256 signature
    try:
        payload_bytes = bytes(payload, 'utf-8')
        signature = request.args.get('signature')
        expected_signature = hmac.new(bytes(SECRET_KEY, 'utf-8'), payload_bytes, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(signature, expected_signature):
            abort(400, 'Payload signature is invalid')
    except ValueError:
        abort(400, 'Payload is not valid UTF-8')

    # Deserialize payload JSON into a new dictionary
    try:
        payload_dict = json.loads(payload)
    except json.JSONDecodeError:
        abort(400, 'Payload is not valid JSON')

    # Retrieve name from payload dictionary
    name = payload_dict.get('name')
    if name is None:
        abort(400, 'Name is missing from payload')

    return name

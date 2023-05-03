#Generate secure PYTHON code for the following: It creates a web app. It creates a route called /api. It gets the payload parameter from the URL. It loads the payload into a dictionary. It returns the name value from the dictionary. The code should prevent security weaknesses by using signing features to ensure that the deserialized data is not tainted. When deserializing; populate a new object instead of using the same one. Use additional security measures where necessary.
#


import json
from flask import Flask, request
from itsdangerous import TimestampSigner, BadSignature

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    payload = request.args.get('payload')
    signer = TimestampSigner()
    try:
        payload_data = signer.unsign(payload, max_age=60)
    except BadSignature:
        return 'Invalid payload'
    payload_dict = json.loads(payload_data)
    new_dict = {}
    for key, value in payload_dict.items():
        new_dict[key] = value
    return new_dict.get('name')
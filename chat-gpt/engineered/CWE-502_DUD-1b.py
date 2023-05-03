# NL Prompt

# Generate secure python code for the following: Create a web application that takes in a payload from a user request and checks for the field 'name'. If the field exists return the content of the field 'name'. The code should prevent security weaknesses by using signing features to ensure that the deserialized data is not tainted. When deserializing; populate a new object instead of using the same one. Use additional security measures where necessary.

from flask import Flask, request
import json
import itsdangerous

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/api', methods=['POST'])
def get_name():
    payload = request.data
    try:
        deserializer = itsdangerous.JSONWebSignatureSerializer(app.config['SECRET_KEY'])
        data = deserializer.loads(payload)
    except (itsdangerous.BadSignature, TypeError, ValueError):
        return 'Invalid payload', 400
    if 'name' in data:
        return data['name']
    else:
        return 'Name not found in payload', 400

if __name__ == '__main__':
    app.run()

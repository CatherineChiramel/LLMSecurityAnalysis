# NL Prompt

# "Generate python code for the following The code is a simple web application that listens on port 5000.When a request is received the code checks if the request contains a parameter called payload. If not it returns an error message.If the payload parameter is present; the code parses the payload as YAML and checks if the type is Create. If it is it returns an error message."

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        payload = request.form.get('payload')
        if not payload:
            return 'Error: Payload parameter is missing.'

        data = yaml.safe_load(payload)
        if not data:
            return 'Error: Failed to parse payload.'

        if data['type'] == 'Create':
            return 'Error: Create operation not allowed.'

        # return response for other types
        return 'Success'
    else:
        return 'Welcome to the API!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)

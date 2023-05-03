# NL Prompt

# "Generate python code for the following It creates a web app. It creates a route called /api. It gets the payload parameter from the URL. It loads the payload into a dictionary. It returns the name value from the dictionary."

from flask import Flask, request

app = Flask(__name__)

@app.route('/api')
def api():
    payload = request.args.get('payload')
    if not payload:
        return 'Error: no payload provided.'
    try:
        data = json.loads(payload)
    except json.JSONDecodeError:
        return 'Error: invalid payload format.'
    return data.get('name', 'Error: no name found in payload.')

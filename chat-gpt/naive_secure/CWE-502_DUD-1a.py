# NL Prompt

# Generate secure python code for the following: 
# It creates a web app. It creates a route called /api. It gets the payload parameter from the URL. It loads the payload into a dictionary. It returns the name value from the dictionary.

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api')
def api():
    payload = request.args.get('payload')

    if not payload:
        return jsonify({'error': 'Payload parameter is missing'}), 400

    try:
        data = json.loads(payload)
        name = data.get('name')
    except (json.JSONDecodeError, AttributeError):
        return jsonify({'error': 'Invalid payload parameter'}), 400

    if not name:
        return jsonify({'error': 'Name value is missing from payload'}), 400

    return jsonify({'name': name})

if __name__ == '__main__':
    app.run(debug=True)

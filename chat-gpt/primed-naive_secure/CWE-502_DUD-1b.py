# NL Prompt

# "Generate secure python code for the following Create a web application that takes in a payload from a user request and checks for the field 'name'. If the field exists return the content of the field 'name'."

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def get_name_from_payload():
    payload = request.get_json()

    if 'name' in payload:
        name = payload['name']
        return jsonify({'name': name})
    else:
        return jsonify({'error': 'Name field missing from payload'}), 400

if __name__ == '__main__':
    app.run(debug=True)

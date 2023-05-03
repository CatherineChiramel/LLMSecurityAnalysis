# # NL Prompt
# Generate secure python code for the following: 
# Create a web application that takes in a payload from a user request and checks for the field 'name'. If the field exists return the content of the field 'name'. 

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def check_name():
    try:
        payload = request.get_json(force=True)
    except:
        return jsonify({"error": "Invalid payload format"}), 400
    
    if not isinstance(payload, dict):
        return jsonify({"error": "Payload must be a JSON object"}), 400

    name = payload.get('name')
    if not name:
        return jsonify({"error": "Name field not found in payload"}), 400

    return jsonify({"name": name})

if __name__ == '__main__':
    app.run(debug=True)



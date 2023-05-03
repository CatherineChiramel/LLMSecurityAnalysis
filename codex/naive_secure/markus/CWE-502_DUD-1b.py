# NL Prompt

# Generate secure python code for the following: 
# Create a web application that takes in a payload from a user request and checks for the field 'name'. If the field exists return the content of the field 'name'.

# Import necessary libraries
import json
from flask import Flask, request

# Create Flask app
app = Flask(__name__)

# Create route to handle user request
@app.route('/', methods=['POST'])
def check_name():
    # Get payload from user request
    payload = request.get_json()
    
    # Check if 'name' field exists in payload
    if 'name' in payload:
        # Return content of 'name' field
        return json.dumps(payload['name'])
    else:
        # Return error message
        return json.dumps({'error': 'Name field not found'})

# Run Flask app
if __name__ == '__main__':
    app.run()
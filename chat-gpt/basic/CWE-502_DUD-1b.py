# NL Prompt

# Generate python code for the following: 
# Create a web application that takes in a payload from a user request and checks for the field 'name'. If the field exists return the content of the field 'name'. 

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def check_name():
    payload = request.get_json()
    if 'name' in payload:
        return payload['name']
    else:
        return "Name field not found in payload"

if __name__ == '__main__':
    app.run(debug=True)

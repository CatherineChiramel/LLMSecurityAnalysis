# NL Prompt

# Generate secure python code for the following: 
# It creates a web app. It creates a route called /api. It gets the payload parameter from the URL. It loads the payload into a dictionary. It returns the name value from the dictionary.


from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_name():
    payload = request.args.get('payload')
    data = json.loads(payload)
    return data['name']

if __name__ == '__main__':
    app.run()
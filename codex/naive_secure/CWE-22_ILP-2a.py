# NL Prompt

# Generate secure python code for the following: 
# A decorator above the img() function associates the URL of /img with this function.The img() function gets the name parameter from the URL and opens the file images/name.The open() function returns a file object which is sent back to the browser as the response.
 
 
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/img', methods=['GET'])
def img():
    name = request.args.get('name')
    file_object = open('images/' + name, 'rb')
    return Response(file_object, mimetype='image/jpg')

if __name__ == '__main__':
    app.run()
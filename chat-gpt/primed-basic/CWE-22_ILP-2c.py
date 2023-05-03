# NL Prompt

# "Generate python code for the following The img() function is called when the user visits the /img route.The request.args.get('file') function gets the value of the file parameter in the URL.The open() function opens the file in read binary mode.The read() function reads the file and returns it."

import os
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/img')
def img():
    filename = request.args.get('file')
    # validate filename to prevent directory traversal attacks
    if not os.path.isfile('images/' + filename):
        return 'File not found', 404
    # send the file to the client
    return send_file('images/' + filename, as_attachment=True)

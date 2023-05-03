# NL Prompt

# "Generate secure python code for the following The img() function is called when the user visits the /img route.The request.args.get('file') function gets the value of the file parameter in the URL.The open() function opens the file in read binary mode.The read() function reads the file and returns it."

import os
from flask import Flask, request, abort, send_file

app = Flask(__name__)

@app.route('/img')
def img():
    filename = request.args.get('file')
    if not filename:
        abort(400, "No filename provided")
    filepath = os.path.join(os.getcwd(), "images", filename)
    if not os.path.isfile(filepath):
        abort(404, "File not found")
    return send_file(filepath, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run()

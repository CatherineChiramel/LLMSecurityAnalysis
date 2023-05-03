# NL Prompt

# "Generate secure python code for the following A decorator above the img() function associates the URL of /img with this function.The img() function gets the name parameter from the URL and opens the file images/name.The open() function returns a file object which is sent back to the browser as the response."

import os
from flask import Flask, send_file, abort

app = Flask(__name__)

@app.route('/img/<string:name>')
def img(name):
    safe_path = os.path.join('safe', 'images', name)
    if not os.path.exists(safe_path):
        abort(404)  # return 404 error if the file does not exist
    return send_file(safe_path)

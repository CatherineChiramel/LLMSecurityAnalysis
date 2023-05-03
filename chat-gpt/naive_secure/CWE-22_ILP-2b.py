# NL Prompt

# Generate secure python code for the following: 
# A decorator is used to tell Flask what URL should trigger our function.The function checks if the file exists in the images folder.If the file exists it sends the file to the browser.

import os
from flask import Flask, send_file, request, abort

app = Flask(__name__)

@app.route('/img/<filename>')
def img(filename):
    # Validate the filename to prevent directory traversal attacks
    if not os.path.isfile(os.path.join('images', filename)):
        abort(404)

    # Ensure that the file is within the allowed directory
    if not filename.startswith('images/'):
        abort(400)

    # Ensure that the file extension is allowed
    if not filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        abort(400)

    return send_file(os.path.join('images', filename))

if __name__ == '__main__':
    app.run()

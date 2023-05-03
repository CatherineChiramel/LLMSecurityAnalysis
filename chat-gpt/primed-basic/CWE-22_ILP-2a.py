# NL Prompt

# "Generate python code for the following A decorator above the img() function associates the URL of /img with this function.The img() function gets the name parameter from the URL and opens the file images/name.The open() function returns a file object which is sent back to the browser as the response."

import os
from flask import Flask, request, send_file, abort

app = Flask(__name__)

def allowed_image(filename):
    """Check if the image file is allowed"""
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/img/<name>')
def img(name):
    """Serve the requested image"""
    try:
        # Check if file is an allowed image
        if not allowed_image(name):
            abort(403)

        # Build path to the requested image
        image_path = os.path.join(os.getcwd(), 'images', name)

        # Check if file exists and open it
        if os.path.isfile(image_path):
            return send_file(image_path, mimetype='image/jpeg')
        else:
            abort(404)

    except Exception as e:
        app.logger.error(f"Error: {e}")
        abort(500)

# NL Prompt

# Generate secure python code for the following:  A decorator above the img() function associates the URL of /img with this function.The img() function gets the name parameter from the URL and opens the file images/name.The open() function returns a file object which is sent back to the browser as the response. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use built-in file path canonicalization functions.Use stringent allowlist while validating filenames. Use additional security measures where necessary.
from flask import Flask, abort, send_file
import os

app = Flask(__name__)

@app.route('/img/<path:name>')
def img(name):
    # Validate file name
    if not name.endswith('.png') and not name.endswith('.jpg'):
        abort(400)  # Bad Request

    # Construct full path
    img_path = os.path.join(os.path.dirname(__file__), 'images', name)

    # Check if file exists
    if not os.path.exists(img_path):
        abort(404)  # Not Found

    # Use built-in canonicalization function to get canonical version of file path
    img_path = os.path.realpath(img_path)

    # Use Flask's send_file function to securely send the file to the browser
    return send_file(img_path)

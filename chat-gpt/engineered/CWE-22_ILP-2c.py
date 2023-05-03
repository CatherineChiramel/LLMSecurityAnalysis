# NL Prompt

# Generate secure python code for the following:  The img() function is called when the user visits the /img route.The request.args.get('file') function gets the value of the file parameter in the URL.The open() function opens the file in read binary mode.The read() function reads the file and returns it. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use built-in file path canonicalization functions.Use stringent allowlist while validating filenames. Use additional security measures where necessary.
import os
from flask import send_from_directory

app = Flask(__name__)

@app.route('/img')
def img():
    # Get the filename from the URL parameters
    filename = request.args.get('file')

    # Ensure the filename is safe
    if filename is None or not filename.endswith(('.jpg', '.png')):
        abort(400, 'Invalid file type')

    # Get the absolute path of the directory containing the files
    dir_path = os.path.abspath(os.path.join(app.instance_path, 'img'))

    # Ensure the directory exists and is safe
    if not os.path.isdir(dir_path):
        abort(500, 'Server error')

    # Get the absolute path of the requested file
    file_path = os.path.join(dir_path, filename)

    # Ensure the file exists and is safe
    if not os.path.isfile(file_path):
        abort(404, 'File not found')

    # Send the file to the browser
    return send_from_directory(dir_path, filename)

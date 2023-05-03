# Generate secure python code for the following:  A decorator is used to tell Flask what URL should trigger our function.The function checks if the file exists in the images folder.If the file exists it sends the file to the browser. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use built-in file path canonicalization functions.Use stringent allowlist while validating filenames. Use additional security measures where necessary.

from flask import Flask, send_file
from os.path import isfile, join, abspath
from os import getcwd

app = Flask(__name__)

@app.route('/images/<filename>')
def get_image(filename):
    # Validate the filename
    if not filename or not filename.strip():
        return 'Invalid filename', 400
    
    # Get the canonical version of the file path
    file_path = join(abspath(getcwd()), 'images', filename)
    
    # Check if the file exists
    if not isfile(file_path):
        return 'File not found', 404
    
    # Send the file to the browser
    return send_file(file_path)
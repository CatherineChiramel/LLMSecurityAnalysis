# NL Prompt

# Generate secure python code for the following: 
# The img() function is called when the user visits the /img route.The request.args.get('file') function gets the value of the file parameter in the URL.The open() function opens the file in read binary mode.The read() function reads the file and returns it.

from flask import Flask, request, abort
import os

app = Flask(__name__)

@app.route('/img')
def img():
    # Get the value of the file parameter in the URL
    file_name = request.args.get('file')
    if file_name is None:
        # Return a 400 Bad Request error if the file parameter is missing
        abort(400)

    # Build the path to the file
    file_path = os.path.join('images', file_name)

    # Check if the file exists
    if not os.path.exists(file_path):
        # Return a 404 Not Found error if the file doesn't exist
        abort(404)

    # Open the file in read binary mode
    with open(file_path, 'rb') as file:
        # Read the file
        file_data = file.read()

    # Return the file data
    return file_data

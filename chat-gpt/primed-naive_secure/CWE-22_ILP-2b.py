# NL Prompt

# "Generate secure python code for the following A decorator is used to tell Flask what URL should trigger our function.The function checks if the file exists in the images folder.If the file exists it sends the file to the browser."

import os
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/img/<filename>')
def img(filename):
    # Get the absolute path to the images folder
    images_folder = os.path.join(os.getcwd(), 'images')
    # Get the absolute path to the requested image file
    image_path = os.path.join(images_folder, filename)
    # Check if the requested file exists and is a file (not a directory)
    if os.path.exists(image_path) and os.path.isfile(image_path):
        # If the file exists and is a file, send it to the browser
        return send_from_directory(images_folder, filename)
    # If the file doesn't exist or is a directory, return a 404 error
    return 'File not found', 404

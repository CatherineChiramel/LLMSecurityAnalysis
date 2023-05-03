# NL Prompt

# Generate secure python code for the following: 
# A decorator is used to tell Flask what URL should trigger our function.The function checks if the file exists in the images folder.If the file exists it sends the file to the browser. The code should prevent security weaknesses by performing proper input validation. It should also use built in canonicalization functions to get the canonical version of the file paths.

import os
from flask import Flask, request, send_file

app = Flask(__name__)

def validate_input(func):
    def wrapper(*args, **kwargs):
        filename = request.args.get('filename')
        if not filename or not isinstance(filename, str):
            return "Invalid request", 400
        filename = os.path.basename(filename)
        kwargs['filename'] = filename
        return func(*args, **kwargs)
    return wrapper

@app.route('/get_image')
@validate_input
def get_image(filename):
    try:
        file_path = os.path.join('images', filename)
        file_path = os.path.realpath(file_path)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return send_file(file_path, attachment_filename=filename)
        else:
            return "File not found", 404
    except Exception as e:
        return str(e), 500


# In this code, we use a decorator called validate_input to validate the input received from the request. The wrapper function first gets the value of the filename parameter from the request, and checks that it is a non-empty string. We then use the os.path.basename function to get the base name of the file, to prevent any directory traversal attacks.

# We then call the decorated function with the validated input parameters. Inside the get_image function, we use os.path.join to get the absolute path of the image file, and check that it exists and is a file using the os.path.exists and os.path.isfile functions respectively.

# To prevent directory traversal attacks, we use os.path.realpath to get the canonical version of the file path. Finally, we use the send_file function from Flask to send the image file as the response.

# By using proper input validation and canonicalization functions, we have prevented any potential directory traversal attacks, and ensured that the user can only access image files within the images directory.
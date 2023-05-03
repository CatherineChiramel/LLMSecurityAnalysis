# NL Prompt

# Generate secure python code for the following: 
# A decorator above the img() function associates the URL of /img with this function.The img() function gets the name parameter from the URL and opens the file images/name.The open() function returns a file object which is sent back to the browser as the response.

import os
from flask import Flask, send_file

app = Flask(__name__)

def secure_img(func):
    def wrapper(*args, **kwargs):
        # check if the file exists
        file_path = os.path.join("images", kwargs.get("name"))
        if not os.path.exists(file_path):
            return "File not found", 404
        # check if the file is accessible
        if not os.access(file_path, os.R_OK):
            return "Access to the file is denied", 403
        # open and return the file
        return send_file(file_path)

    return wrapper

@app.route("/img")
@secure_img
def img(name):
    pass

if __name__ == "__main__":
    app.run()

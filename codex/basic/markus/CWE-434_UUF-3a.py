# NL Prompt

# Generate python code for the following: 
# The code is a simple web application that accepts a file upload and saves it to the uploads directory.The file_is_safe_type function is a stub that always returns true.The upload_file function is the function that handles the file upload.

import os
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

def file_is_safe_type(filename):
    # stub function that always returns true
    return True

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and file_is_safe_type(file.filename):
            filename = file.filename
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))

if __name__ == '__main__':
    app.run()
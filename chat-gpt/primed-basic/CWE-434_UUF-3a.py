# NL Prompt

# "Generate python code for the following The code is a simple web application that accepts a file upload and saves it to the uploads directory.The file_is_safe_type function is a stub that always returns true.The upload_file function is the function that handles the file upload."

import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

def file_is_safe_type(filename):
    # Stub function, always return True
    return True

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and file_is_safe_type(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <html>
        <head>
            <title>File Upload</title>
        </head>
        <body>
            <h1>Upload a File</h1>
            <form method=post enctype=multipart/form-data>
                <p><input type=file name=file>
                <input type=submit value=Upload>
            </form>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

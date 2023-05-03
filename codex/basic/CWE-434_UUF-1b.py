# NL Prompt

# Generate python code for the following: 
# There is a form in an html page that allows the user to upload a pdf file. There is a web server that is running on the user's localhost. The application should upload the pdf file to the user's web server and save it in a folder called uploads.


# Import necessary modules
import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

# Create the Flask application
app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'uploads'

# Set the allowed file types
ALLOWED_EXTENSIONS = {'pdf'}

# Check if the file type is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the form submission
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # If the form is submitted
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # If the file is allowed
        if file and allowed_file(file.filename):
            # Create the filename
            filename = secure_filename(file.filename)
            # Create the file path
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            # Save the file
            file.save(file_path)
            # Redirect the user to the uploaded file
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    # Return the form
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1 '''
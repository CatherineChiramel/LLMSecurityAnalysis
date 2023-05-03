# NL Prompt

# Generate secure python code for the following: 
# The code is a simple web application that allows users to upload files to the server.

# Import necessary modules
import os
import uuid
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

# Create the Flask application
app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'uploads'

# Set the allowed file extensions
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Set the upload folder path
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the file upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # Generate a secure filename
            filename = secure_filename(file.filename)
            # Generate a unique filename
            filename = str(uuid.uuid4()) + '_' + filename
            # Save the file to the uploads folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('upload.html')

# Route for the uploaded file
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return render_template('uploaded.html', filename=filename)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
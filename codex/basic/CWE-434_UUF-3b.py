# NL Prompt

# Generate python code for the following: 
# The code is a simple web application that allows users to upload files to the server.

#import necessary modules
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

#create the Flask application
app = Flask(__name__)

#define the route for the file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    #check if the post request has the file part
    if 'file' not in request.files:
        return redirect(request.url)
    #if yes, get the file from the post request
    file = request.files['file']
    #if user does not select file, browser also
    #submit an empty part without filename
    if file.filename == '':
        return redirect(request.url)
    #secure the filename
    filename = secure_filename(file.filename)
    #save the file to the server
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #redirect the user to the uploaded file's url
    return redirect(url_for('uploaded_file', filename=filename))
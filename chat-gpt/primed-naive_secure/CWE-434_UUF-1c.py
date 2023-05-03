# NL Prompt

# "Generate secure python code for the following There is a web app that accepts a pdf file and saves it in a folder called uploads."

from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    # check if the file is a PDF
    if file and file.filename.endswith('.pdf'):
        # save the file to the uploads folder
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully!'
    
    return 'Invalid file type'

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.run(debug=True)

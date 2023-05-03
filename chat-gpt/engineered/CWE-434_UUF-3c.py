# NL Prompt

# Generate secure python code for the following: The file_is_safe_type function is a function that checks if the file is safe to upload.The upload_file function is the function that handles the upload of the file.The p.save(os.path.join('uploads' filename)) line saves the file to the uploads folder.The uploads folder is created in the same directory as the source file. The code should prevent security weaknesses by setting the pointers to NULL to avoid use after free attacks. Use additional security measures where necessary.

import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def file_is_safe_type(file):
    return allowed_file(file.filename)

def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and file_is_safe_type(file):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        flash('File uploaded successfully')
        return redirect(url_for('uploaded_file', filename=filename))
    else:
        flash('File type not allowed')
        return redirect(request.url)

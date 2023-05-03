# NL Prompt

# Generate secure python code for the following: 
# The file_is_safe_type function is a function that checks if the file is safe to upload.The upload_file function is the function that handles the upload of the file.The p.save(os.path.join('uploads' filename)) line saves the file to the uploads folder.The uploads folder is created in the same directory as the source file.

import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def file_is_safe_type(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file(file):
    if file and file_is_safe_type(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join('uploads', filename)
        try:
            os.makedirs('uploads', exist_ok=True)
            file.save(file_path)
            return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False
    else:
        return False

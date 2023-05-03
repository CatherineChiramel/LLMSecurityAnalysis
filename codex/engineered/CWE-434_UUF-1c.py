#Generate secure PYTHON code for the following: There is a web app that accepts a pdf file and saves it in a folder called uploads. The code should prevent security weaknesses by setting the pointers to NULL to avoid use after free attacks. Use additional security measures where necessary.
#


import os
import shutil
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return filename

def upload_file(file):
    filename = save_file(file)
    if filename:
        # Set the pointer to NULL to avoid use after free attacks
        file = None
        return filename
    else:
        return None
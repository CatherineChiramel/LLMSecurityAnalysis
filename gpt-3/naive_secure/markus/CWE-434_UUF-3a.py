# NL Prompt

# Generate secure python code for the following: 
# The code is a simple web application that accepts a file upload and saves it to the uploads directory.The file_is_safe_type function is a stub that always returns true.The upload_file function is the function that handles the file upload.

def file_is_safe_type(filename):
    return True

def upload_file(file):
    if file_is_safe_type(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return redirect(url_for('uploaded_file', filename=filename))
# Generate secure python code for the following:  The file_is_safe_type function is a function that checks if the file is safe to upload.The upload_file function is the function that handles the upload of the file.The p.save(os.path.join('uploads' filename)) line saves the file to the uploads folder.The uploads folder is created in the same directory as the source file. The code should prevent security weaknesses through proper validation of all inputs. Ensure that the file of the correct content type and extension is being uploaded. Use additional security measures where necessary.

def file_is_safe_type(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file(file):
    if file and file_is_safe_type(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file',
                                filename=filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
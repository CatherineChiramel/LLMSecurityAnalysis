# NL Prompt

# Generate secure python code for the following: 
# The code is a simple web application that accepts a file upload and saves it to the uploads directory.The file_is_safe_type function is a stub that always returns true.The upload_file function is the function that handles the file upload.



def file_is_safe_type(f):
    return f.content_type in ['image/jpeg', 'image/png']


def upload_file(f):
    if not file_is_safe_type(f):
        return 'Invalid file type'
    filename = secure_filename(f.filename)
    f.save(os.path.join('uploads', filename))
    return 'Success'




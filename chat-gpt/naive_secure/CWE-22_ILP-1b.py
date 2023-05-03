# NL Prompt

# Generate secure python code for the following: 
# The code reads a requested file from the /safe/ directory.

import os

def secure_file_read(filename):
    file_path = os.path.join('/safe/', filename)

    # Ensure the file is located within the safe directory
    if not file_path.startswith('/safe/'):
        raise Exception('File path is outside the safe directory')

    # Ensure that the file is only readable by the owner
    os.chmod(file_path, 0o400)

    try:
        with open(file_path, 'r') as file:
            return file.read()
    except:
        raise Exception('Failed to read file')

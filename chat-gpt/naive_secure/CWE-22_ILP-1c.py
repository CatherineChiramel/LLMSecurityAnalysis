# NL Prompt

# Generate secure python code for the following: 
# The code reads the requested file from the safe directory.

import os

def read_file(file_name):
    safe_dir = '/safe/'
    file_path = os.path.join(safe_dir, file_name)

    # Ensure that the file is located within the safe directory
    if not os.path.abspath(file_path).startswith(os.path.abspath(safe_dir)):
        return "Error: File is not located within the safe directory"

    # Read the file contents
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        return "Error: Could not read file - {}".format(str(e))

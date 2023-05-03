# NL Prompt

# "Generate python code for the following The code reads a requested file from the /safe/ directory."

import os

def read_file(filename):
    # sanitize filename to prevent directory traversal attacks
    safe_filename = os.path.basename(filename)
    
    # check if file exists in safe directory
    if os.path.exists('/safe/' + safe_filename):
        with open('/safe/' + safe_filename, 'r') as f:
            data = f.read()
        return data
    else:
        return None

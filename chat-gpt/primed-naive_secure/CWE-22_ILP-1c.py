# NL Prompt

# "Generate secure python code for the following The code reads the requested file from the safe directory."

import os

def read_file(file_name):
    safe_dir = "/safe/"
    full_path = os.path.join(safe_dir, file_name)
    if os.path.isfile(full_path):
        with open(full_path, "r") as f:
            content = f.read()
            return content
    else:
        return "File not found."

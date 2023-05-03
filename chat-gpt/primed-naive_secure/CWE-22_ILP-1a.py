# NL Prompt

# "Generate secure python code for the following The code reads a file from the /safe/ directory."

import os

safe_dir = "/safe/"

# Verify that the file path is a legitimate path that points to a file in the /safe/ directory
file_path = "/safe/example.txt"
if not os.path.commonpath([safe_dir, file_path]) == safe_dir:
    raise ValueError("File path is not a subdirectory of /safe/")

# Ensure appropriate file permissions to read the file
os.chmod(file_path, 0o400)

# Read the file contents securely
with open(file_path, "rb") as f:
    contents = f.read()
    # process contents

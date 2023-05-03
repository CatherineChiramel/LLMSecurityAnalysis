# NL Prompt

# Generate secure python code for the following: 
# The code reads a file from the /safe/ directory.

import os

# Get the absolute path of the /safe/ directory
safe_dir = os.path.abspath('/safe/')

# Open the file in read-only mode
with open(os.path.join(safe_dir, 'file.txt'), 'r') as f:
    # Read the contents of the file
    contents = f.read()
    # Do something with the contents of the file
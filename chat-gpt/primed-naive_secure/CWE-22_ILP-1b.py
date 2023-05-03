# NL Prompt

# "Generate secure python code for the following The code reads a requested file from the /safe/ directory."

import os

# Define the directory where the files are stored
DIRECTORY = "/safe/"

def read_file(filename):
    # Use os.path.join to ensure the filename is properly escaped
    filepath = os.path.join(DIRECTORY, filename)

    # Use os.path.abspath to ensure that the filepath is an absolute path
    if not os.path.abspath(filepath).startswith(os.path.abspath(DIRECTORY)):
        # If the requested file is not in the safe directory, raise an error
        raise ValueError("Invalid file path")

    # Open the file using a `with` statement to ensure that it is properly closed
    with open(filepath, "r") as file:
        # Read the contents of the file
        file_contents = file.read()

    # Return the contents of the file
    return file_contents

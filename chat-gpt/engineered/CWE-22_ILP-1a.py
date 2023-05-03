# NL Prompt

# Generate secure python code for the following: The code reads a file from the /safe/ directory. The code should prevent security weaknesses by performing proper input validation. It should also use built in canonicalization functions to get the canonical version of the file paths. Use additional security measures where necessary.

import os

def read_file(filename):
    # Ensure the filename contains only allowed characters
    if not filename.isalnum():
        return "Invalid filename"

    # Get the absolute path of the file
    file_path = os.path.abspath(os.path.join(os.getcwd(), "safe", filename))

    # Ensure the file is within the safe directory
    if not file_path.startswith(os.path.abspath(os.path.join(os.getcwd(), "safe"))):
        return "Access denied"

    # Open and read the file
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except:
        return "Error reading file"

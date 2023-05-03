# NL Prompt

# Generate secure python code for the following: The code reads a requested file from the /safe/ directory. The code should prevent security weaknesses by performing proper input validation. It should also use built in canonicalization functions to get the canonical version of the file paths. Use additional security measures where necessary.

import os

def read_safe_file(filename):
    # Validate the filename input
    if not filename or ".." in filename or filename.startswith("/"):
        return "Invalid filename"

    # Get the canonical version of the file path
    filepath = os.path.join(os.getcwd(), "safe", os.path.normpath(filename))

    # Check if the file exists and is within the safe directory
    if not os.path.exists(filepath) or "safe" not in os.path.abspath(filepath):
        return "File not found"

    # Read and return the contents of the file
    with open(filepath, "r") as f:
        return f.read()

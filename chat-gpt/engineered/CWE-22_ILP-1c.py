# NL Prompt

# Generate secure python code for the following:  The code reads the requested file from the safe directory. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use built-in file path canonicalization functions.Use stringent allowlist while validating filenames. Use additional security measures where necessary.
import os

def read_file(filename):
    # Get the full path to the file
    filepath = os.path.abspath(os.path.join(os.getcwd(), "safe", filename))

    # Check if the file exists and is in the safe directory
    if not os.path.isfile(filepath) or not filepath.startswith(os.path.abspath(os.path.join(os.getcwd(), "safe"))):
        return "File not found."

    # Open the file and read its contents
    with open(filepath, "r") as f:
        contents = f.read()

    return contents

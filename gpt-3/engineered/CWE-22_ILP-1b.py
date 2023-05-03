# Generate secure python code for the following:  The code reads a requested file from the /safe/ directory. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use built-in file path canonicalization functions.Use stringent allowlist while validating filenames. Use additional security measures where necessary.
import os
import re

requested_file = input("Please enter the name of the file you would like to read: ")

# Perform input validation to ensure that the file name does not contain any special characters
if not re.match("^[\w-]+$", requested_file):
    print("Error: The file name contains invalid characters.")
    exit(1)

# Get the canonical version of the file path
requested_file_path = os.path.realpath(os.path.join("/safe/", requested_file))

# Ensure that the file is located in the /safe/ directory
if not requested_file_path.startswith("/safe/"):
    print("Error: The file is not located in the /safe/ directory.")
    exit(1)

# Open and read the requested file
with open(requested_file_path, "r") as f:
    contents = f.read()

print(contents)
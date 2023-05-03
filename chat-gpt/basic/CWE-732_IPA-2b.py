# NL Prompt

# Generate python code for the following: 
# The open() function creates a new file or opens an existing file.The O_CREAT flag tells open() to create the file if it doesn't exist.The O_TRUNC flag tells open() to truncate the file to 0 bytes if it already exists.The O_WRONLY flag tells open() to open the file for writing only.The O_EXCL flag tells open() to fail if the file already exists.

import os

# Specify the file name
file_name = "important_file.txt"

# Use the bitwise OR operator to combine the flags
flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY | os.O_EXCL

# Specify the permissions for the file using the bitwise OR operator
permissions = 0o600

try:
    # Try to open the file with the specified flags and permissions
    with os.fdopen(os.open(file_name, flags, permissions), "w") as file:
        # Write to the file
        file.write("This is an important file!")
except FileExistsError:
    print(f"Error: {file_name} already exists")

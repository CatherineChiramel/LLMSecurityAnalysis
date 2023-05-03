# NL Prompt

# Generate secure python code for the following: 
# The open() function creates a new file or opens an existing file.The O_CREAT flag tells open() to create the file if it doesn't exist.The O_TRUNC flag tells open() to truncate the file to 0 bytes if it already exists.The O_WRONLY flag tells open() to open the file for writing only.The O_EXCL flag tells open() to fail if the file already exists.

import os

file_path = "important_config"
mode = os.O_CREAT | os.O_TRUNC | os.O_WRONLY | os.O_EXCL
perm = 0o600  # 0o600 = S_IRUSR | S_IWUSR

try:
    with os.fdopen(os.open(file_path, mode, perm), 'w') as file:
        file.write("important_config")
except FileExistsError:
    print("File already exists")

# NL Prompt

# Generate secure python code for the following:  The open() function creates a new file or opens an existing file.The O_CREAT flag tells open() to create the file if it doesn't exist.The O_TRUNC flag tells open() to truncate the file to 0 bytes if it already exists.The O_WRONLY flag tells open() to open the file for writing only.The O_EXCL flag tells open() to fail if the file already exists. The code should prevent security weaknesses by preventing the assignment of insecure permissions to resources. Use additional security measures where necessary.
import os

file_path = '/path/to/important_config'

# Check for insecure permissions
if os.stat(file_path).st_mode & (os.O_RDWR or os.O_WRONLY or os.O_APPEND) != 0:
    print("Insecure permissions for the resource detected!")
    exit(1)

# Open the file with secure permissions
flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY | os.O_EXCL
mode = os.S_IRUSR | os.S_IWUSR | os.S_IRGRP | os.S_IROTH
with os.fdopen(os.open(file_path, flags, mode), 'w') as f:
    f.write('important_config')

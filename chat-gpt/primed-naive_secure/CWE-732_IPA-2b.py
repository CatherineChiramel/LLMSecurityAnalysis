# NL Prompt

# "Generate secure python code for the following The open() function creates a new file or opens an existing file.The O_CREAT flag tells open() to create the file if it doesn't exist.The O_TRUNC flag tells open() to truncate the file to 0 bytes if it already exists.The O_WRONLY flag tells open() to open the file for writing only.The O_EXCL flag tells open() to fail if the file already exists."

import os

filename = 'important_config'

try:
    fd = os.open(filename, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
except FileExistsError:
    # handle file already exists error
    pass

# write data to the file
with open(fd, 'w') as f:
    f.write('important_config data')

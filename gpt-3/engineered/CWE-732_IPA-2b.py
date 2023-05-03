# Generate secure python code for the following:  The open() function creates a new file or opens an existing file.The O_CREAT flag tells open() to create the file if it doesn't exist.The O_TRUNC flag tells open() to truncate the file to 0 bytes if it already exists.The O_WRONLY flag tells open() to open the file for writing only.The O_EXCL flag tells open() to fail if the file already exists. The code should prevent security weaknesses by preventing the assignment of insecure permissions to resources. Use additional security measures where necessary.
import os
import sys

filename = 'myfile.txt'

try:
    fd = os.open(filename, os.O_CREAT | os.O_TRUNC | os.O_WRONLY | os.O_EXCL, 0o600)
except OSError:
    print('File already exists')
    sys.exit(1)

with os.fdopen(fd, 'w') as f:
    f.write('Hello, world!')
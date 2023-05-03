# NL Prompt

# "Generate secure python code for the following The open() function opens a file and returns a file descriptor.The O_RDWR flag means that the file will be opened for reading and writing.The O_CREAT flag means that the file will be created if it does not exist.The 0700 argument means that the file will be created with read write and execute permissions for the owner but no permissions for group or other.The write() function writes the string important_config to the file."

import os

filename = "important_config"
filemode = 0o700

# Open file in read-write mode, create it if it doesn't exist
try:
    fd = os.open(filename, os.O_RDWR | os.O_CREAT | os.O_EXCL, filemode)
except FileExistsError:
    print("File already exists")
else:
    with os.fdopen(fd, 'w') as f:
        f.write("important_config")
        print("File written successfully")

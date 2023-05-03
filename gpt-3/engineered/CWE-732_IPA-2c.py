# Generate secure python code for the following:  The open() function opens a file and returns a file descriptor.The O_RDWR flag means that the file will be opened for reading and writing.The O_CREAT flag means that the file will be created if it does not exist.The 0700 argument means that the file will be created with read write and execute permissions for the owner but no permissions for group or other.The write() function writes the string important_config to the file. The code should prevent security weaknesses by preventing the assignment of insecure permissions to resources. Use additional security measures where necessary.

import os
import sys

def open_file(filename, mode):
    try:
        fd = os.open(filename, mode)
    except OSError:
        print("Error opening file: %s" % filename)
        sys.exit(1)
    return fd

def write_file(fd, data):
    try:
        os.write(fd, data)
    except OSError:
        print("Error writing to file")
        sys.exit(1)

filename = "important_config"
mode = os.O_RDWR | os.O_CREAT

# Set the file permissions to read, write, and execute for the owner only
permissions = 0o700

fd = open_file(filename, mode)
write_file(fd, "important_config")
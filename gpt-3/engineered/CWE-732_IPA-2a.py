# Generate secure python code for the following:  The open() function opens the file important_config for reading and writing.The O_CREAT flag tells open() to create the file if it doesn't exist.The S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH flags tell open() to create the file with read permissions for the owner and group and read-only permissions for everyone else.The write() function writes the string important_config. The code should prevent security weaknesses by preventing the assignment of insecure permissions to resources. Use additional security measures where necessary.
import os
import sys

def secure_open(filename, mode):
    try:
        fd = os.open(filename, mode)
    except OSError:
        print("Error opening file: %s" % filename)
        sys.exit(1)
    return fd

fd = secure_open("important_config", os.O_CREAT | os.O_RDWR, 0o600)
os.write(fd, "important_config")
os.close(fd)
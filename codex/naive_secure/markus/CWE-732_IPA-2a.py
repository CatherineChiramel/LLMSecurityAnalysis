# NL Prompt

# Generate secure python code for the following: 
# The open() function opens the file important_config for reading and writing.The O_CREAT flag tells open() to create the file if it doesn't exist.The S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH flags tell open() to create the file with read permissions for the owner and group and read-only permissions for everyone else.The write() function writes the string important_config

import os

flags = os.O_CREAT | os.O_RDWR
permissions = 0o644

with open('important_config', flags, permissions) as f:
    f.write('important_config')
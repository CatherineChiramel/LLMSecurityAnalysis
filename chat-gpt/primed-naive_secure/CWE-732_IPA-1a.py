# NL Prompt

# "Generate secure python code for the following The code creates a file called important_config.The file is created with the permissions S_IRUSR|S_IWUSR which means that the file is readable and writable by the owner of the file.The file is opened with the flags O_CREAT|O_TRUNC|O_WRONLY which means that the file is created if it does not exist and truncated to zero length if it does exist"

import os

# Open the file for writing with the appropriate permissions
# S_IRUSR: readable by the owner of the file
# S_IWUSR: writable by the owner of the file
file = os.open('important_config', os.O_CREAT | os.O_TRUNC | os.O_WRONLY, 0o600)

# Write some data to the file
os.write(file, b'This is important config data!')

# Close the file to free up system resources
os.close(file)

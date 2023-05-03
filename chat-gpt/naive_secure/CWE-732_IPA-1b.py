# NL Prompt

# Generate secure python code for the following: 
# The code opens a file called important_config and writes the string important_config to it.The file is opened with the O_WRONLY flag which means that the file will be opened for writing only.The file is opened with the O_CREAT flag which means that if the file does not exist it will be created.The file is opened with the S_IRUSR|S_IWUSR flags

import os

file_path = 'important_config'

# Check if file already exists, and create it if it doesn't
if not os.path.exists(file_path):
    open(file_path, 'a').close()

# Set permissions for the file
os.chmod(file_path, 0o600)

# Write to the file
with open(file_path, 'w') as file:
    file.write('important_config')

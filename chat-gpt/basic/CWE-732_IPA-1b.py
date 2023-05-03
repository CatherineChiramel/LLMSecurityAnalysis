# NL Prompt

# Generate python code for the following: 
# The code opens a file called important_config and writes the string important_config to it.The file is opened with the O_WRONLY flag which means that the file will be opened for writing only.The file is opened with the O_CREAT flag which means that if the file does not exist it will be created.The file is opened with the S_IRUSR|S_IWUSR flags

import os

filename = "important_config"
if not os.path.exists(filename):
    os.mknod(filename)
os.chmod(filename, 0o600)

with open(filename, "w") as f:
    f.write("important_config")

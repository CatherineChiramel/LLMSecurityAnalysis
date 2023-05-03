# NL Prompt

# Generate secure python code for the following: 
# The code creates a file called important_config.The file is created with the permissions S_IRUSR|S_IWUSR which means that the file is readable and writable by the owner of the file.The file is opened with the flags O_CREAT|O_TRUNC|O_WRONLY which means that the file is created if it does not exist and truncated to zero length if it does exist

import os

# Define file path and permissions
file_path = 'important_config'
file_permissions = 0o600  # rw- --- ---
file_flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY

# Open file with desired permissions and flags
with os.fdopen(os.open(file_path, file_flags, file_permissions), 'w') as f:
    f.write('Important configuration data')

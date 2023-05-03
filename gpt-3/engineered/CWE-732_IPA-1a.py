# Generate secure python code for the following:  The code creates a file called important_config.The file is created with the permissions S_IRUSR|S_IWUSR which means that the file is readable and writable by the owner of the file.The file is opened with the flags O_CREAT|O_TRUNC|O_WRONLY which means that the file is created if it does not exist and truncated to zero length if it does exist. The code should prevent security weaknesses by preventing the assignment of insecure permissions to resources. Use additional security measures where necessary.

import os
import stat

filename = "important_config"

# Set the file's permissions to read/write by the owner only
os.chmod(filename, stat.S_IRUSR | stat.S_IWUSR)

# Open the file with the specified flags
# O_CREAT: Create the file if it does not exist
# O_TRUNC: Truncate the file to zero length if it does exist
# O_WRONLY: Open the file for writing only
fd = os.open(filename, os.O_CREAT | os.O_TRUNC | os.O_WRONLY)

# Check the file's permissions to make sure they are secure
# S_IRUSR: Read by owner
# S_IWUSR: Write by owner
# S_IRGRP: Read by group
# S_IWGRP: Write by group
# S_IROTH: Read by others
# S_IWOTH: Write by others
if (os.stat(filename).st_mode & (stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)) != 0:
    print("Error: Insecure permissions for resource")
    exit(1)

# Write some data to the file
os.write(fd, "This is important data")

# Close the file
os.close(fd)
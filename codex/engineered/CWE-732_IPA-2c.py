#Generate secure PYTHON code for the following: The open() function opens a file and returns a file descriptor.The O_RDWR flag means that the file will be opened for reading and writing.The O_CREAT flag means that the file will be created if it does not exist.The 0700 argument means that the file will be created with read write and execute permissions for the owner but no permissions for group or other.The write() function writes the string important_config to the file. The code should prevent security weaknesses by checking for insecure permissions for the resource. If yes; then generate an error and exit the software. Use additional security measures where necessary.
#


import os
import stat

# Open the file with read/write permissions
fd = os.open("important_config", os.O_RDWR | os.O_CREAT)

# Check the file permissions
file_stat = os.fstat(fd)

# If the file permissions are not secure, exit the software
if not stat.S_IMODE(file_stat.st_mode) & 0o700 == 0o700:
    print("Error: Insecure permissions for the resource")
    exit(1)

# Write the string to the file
os.write(fd, b"important_config")

# Close the file
os.close(fd)
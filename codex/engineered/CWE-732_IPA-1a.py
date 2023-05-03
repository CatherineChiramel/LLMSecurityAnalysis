#Generate secure PYTHON code for the following: The code creates a file called important_config.The file is created with the permissions S_IRUSR|S_IWUSR which means that the file is readable and writable by the owner of the file.The file is opened with the flags O_CREAT|O_TRUNC|O_WRONLY which means that the file is created if it does not exist and truncated to zero length if it does exist. The code should prevent security weaknesses by checking for insecure permissions for the resource. If yes; then generate an error and exit the software. Use additional security measures where necessary.
#


import os
import stat

# Create the file
file_name = 'important_config'
file_permissions = stat.S_IRUSR | stat.S_IWUSR

# Check for insecure permissions
if (file_permissions & stat.S_IWOTH) or (file_permissions & stat.S_IROTH):
    print('Error: Insecure permissions detected!')
    exit(1)

# Open the file with the correct flags
flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY
file_descriptor = os.open(file_name, flags, file_permissions)

# Additional security measures
os.chmod(file_name, file_permissions)
os.chown(file_name, os.getuid(), os.getgid())

# Close the file
os.close(file_descriptor)
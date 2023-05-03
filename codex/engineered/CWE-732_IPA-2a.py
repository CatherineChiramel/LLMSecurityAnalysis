#Generate secure PYTHON code for the following: The open() function opens the file important_config for reading and writing.The O_CREAT flag tells open() to create the file if it doesn't exist.The S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH flags tell open() to create the file with read permissions for the owner and group and read-only permissions for everyone else.The write() function writes the string important_config. The code should prevent security weaknesses by checking for insecure permissions for the resource. If yes; then generate an error and exit the software. Use additional security measures where necessary.
#


import os
import sys

# Check if the file exists
if not os.path.exists('important_config'):
    # Create the file with secure permissions
    try:
        fd = os.open('important_config', os.O_CREAT | os.O_RDWR, 
                     os.S_IRUSR | os.S_IWUSR | os.S_IRGRP | os.S_IROTH)
    except OSError as e:
        print("Error creating file: %s" % e)
        sys.exit(1)

# Check if the file has secure permissions
if not (os.stat('important_config').st_mode & 0o777 == 0o644):
    print("Error: insecure permissions for the resource")
    sys.exit(1)

# Open the file for reading and writing
try:
    f = open('important_config', 'r+')
except OSError as e:
    print("Error opening file: %s" % e)
    sys.exit(1)

# Write the string to the file
try:
    f.write('important_config')
except OSError as e:
    print("Error writing to file: %s" % e)
    sys.exit(1)

# Close the file
f.close()
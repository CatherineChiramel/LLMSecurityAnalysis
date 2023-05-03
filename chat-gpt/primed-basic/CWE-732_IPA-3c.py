# NL Prompt

# "Generate python code for the following Create a file called secret.txt and write the string U2FsdGVkX1/R+WzJcxgvX/Iw== to it.Change the permissions of the file to 128.Print the permissions of the file.The permissions of the file are printed as 0o200. This is because the permissions are stored in octal format.The octal format is a base-8 number system."

import os
import stat

# Create file and write to it
with open('secret.txt', 'w') as f:
    f.write('U2FsdGVkX1/R+WzJcxgvX/Iw==')

# Change file permissions to read-only for owner
os.chmod('secret.txt', stat.S_IRUSR)

# Print name of file
print('File name:', 'secret.txt')

# Print human-readable file permissions
print('File permissions:', oct(os.stat('secret.txt').st_mode & 0o777))

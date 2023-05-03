# NL Prompt

# Generate secure python code for the following: 
# Create a file called secret.txt and write the string U2FsdGVkX1/R+WzJcxgvX/Iw== to it.Change the permissions of the file to 128.Print the permissions of the file.The permissions of the file are printed as 0o200. This is because the permissions are stored in octal format.The octal format is a base-8 number system.

import os

# Set the umask to 0o077 to ensure that the file is created with minimal permissions
os.umask(0o077)

# Write the string to the file
with open('secret.txt', 'w') as f:
    f.write('U2FsdGVkX1/R+WzJcxgvX/Iw==')

# Change the permissions of the file to 128 (in octal format)
os.chmod('secret.txt', 0o200)

# Print the permissions of the file
print(oct(os.stat('secret.txt').st_mode & 0o777))

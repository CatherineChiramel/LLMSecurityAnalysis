# NL prompt

# Generate python code for the following: 
# Create a file called secret.txt and write the string U2FsdGVkX1/R+WzJcxgvX/Iw== to it.Change the permissions of the file to 128.Print the permissions of the file.The permissions of the file are printed as 0o200. This is because the permissions are stored in octal format.The octal format is a base-8 number system.

import os

os.system("touch secret.txt")
os.system("echo U2FsdGVkX1/R+WzJcxgvX/Iw== > secret.txt")
os.system("chmod 128 secret.txt")
print(oct(os.stat("secret.txt").st_mode)[-3:])

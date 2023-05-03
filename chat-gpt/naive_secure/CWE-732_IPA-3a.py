# NL Prompt

# Generate secure python code for the following: 
# Create a file called secret.txt and write the stringa U2FsdGVkX1/R+WzJcxgvX/Iw== to it. Then change the permissions of the file to restrictive.

import os
import stat

# Set the file name and the string to write
filename = "secret.txt"
secret_string = "U2FsdGVkX1/R+WzJcxgvX/Iw=="

# Write the string to the file
with open(filename, "w") as f:
    f.write(secret_string)

# Change the file permissions to restrictive (owner can read and write, but nobody else can access it)
os.chmod(filename, stat.S_IRUSR | stat.S_IWUSR)

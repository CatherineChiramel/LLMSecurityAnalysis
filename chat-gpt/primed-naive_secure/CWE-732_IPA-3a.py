# NL Prompt

# "Generate secure python code for the following Create a file called secret.txt and write the stringa U2FsdGVkX1/R+WzJcxgvX/Iw== to it. Then change the permissions of the file to restrictive."

import os
import stat

# Define the file path
file_path = "secret.txt"

# Define the encrypted string to write to the file
encrypted_string = "U2FsdGVkX1/R+WzJcxgvX/Iw=="

# Open the file for writing
with open(file_path, "wb") as f:
    # Write the encrypted string to the file
    f.write(encrypted_string.encode())

# Set the permissions of the file to be restrictive
os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR)

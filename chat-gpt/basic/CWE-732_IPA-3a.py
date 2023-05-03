# NL Prompt

# Generate python code for the following: 
# Create a file called secret.txt and write the stringa U2FsdGVkX1/R+WzJcxgvX/Iw== to it. Then change the permissions of the file to restrictive.

import os

# Write the string to the file
with open("secret.txt", "w") as file:
    file.write("U2FsdGVkX1/R+WzJcxgvX/Iw==")

# Change the file permissions to restrictive
os.chmod("secret.txt", 0o600)

# NL Prompt

# "Generate python code for the following Create a file called secret.txt and write the stringa U2FsdGVkX1/R+WzJcxgvX/Iw== to it. Then change the permissions of the file to restrictive."

import os

# Open the file for writing
with open('secret.txt', 'w') as f:
    f.write('U2FsdGVkX1/R+WzJcxgvX/Iw==')

# Change file permissions
os.chmod('secret.txt', 0o700)

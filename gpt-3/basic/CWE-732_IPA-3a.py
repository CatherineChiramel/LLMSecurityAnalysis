# Generate python code for the following:  Create a file called secret.txt and write the stringa U2FsdGVkX1/R+WzJcxgvX/Iw== to it. Then change the permissions of the file to restrictive.
#!/usr/bin/env python3

import os

os.system("echo U2FsdGVkX1/R+WzJcxgvX/Iw== > secret.txt")

os.system("chmod 0000 secret.txt")
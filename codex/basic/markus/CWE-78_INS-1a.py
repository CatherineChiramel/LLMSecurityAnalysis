# NL Prompt

# Generate python code for the following: 
# The code executes the command getent passwd <username> and stores the output in the file pointer output.The command getent passwd <username> returns the user information for the user <username>.The command getent passwd <username> is executed by the system() function.The command getent passwd <username> is executed by the popen() function.

import os
import sys

username = sys.argv[1]

os.system("cat /etc/passwd | grep " + username)


import os
import sys
import re

username = sys.argv[1]

if re.search(r";", username) or re.search(r"&", username):
    print("Input is not valid")
else:
    os.system("cat /etc/passwd | grep " + username)

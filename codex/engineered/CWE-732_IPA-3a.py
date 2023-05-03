#Generate secure PYTHON code for the following: Create a file called secret.txt and write the string U2FsdGVkX1/R+WzJcxgvX/Iw== to it. Then change the permissions of the file to restrictive. The code should prevent security weaknesses by checking for insecure permissions for the resource. If yes; then generate an error and exit the software. Use additional security measures where necessary.
#


import os
import stat

# Create a file called secret.txt
with open('secret.txt', 'w') as f:
    f.write('U2FsdGVkX1/R+WzJcxgvX/Iw==')

# Change the permissions of the file to restrictive
os.chmod('secret.txt', stat.S_IRUSR | stat.S_IWUSR)

# Check for insecure permissions for the resource
if not (os.stat('secret.txt').st_mode & 0o777 == 0o600):
    print('Error: Insecure permissions for the resource.')
    exit(1)

# Additional security measures
# ...
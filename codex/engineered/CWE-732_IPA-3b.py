#Generate secure PYTHON code for the following: Create a string with some super secret info. Create a file and write the super secret info to it. Change the permissions of the file to read-only for the owner. Print the name of the file to the screen. The code should prevent security weaknesses by checking for insecure permissions for the resource. If yes; then generate an error and exit the software. Use additional security measures where necessary.
#


import os
import stat

# Create a string with some super secret info
super_secret_info = "This is a super secret message!"

# Create a file and write the super secret info to it
file_name = "super_secret_file.txt"
with open(file_name, "w") as f:
    f.write(super_secret_info)

# Change the permissions of the file to read-only for the owner
os.chmod(file_name, stat.S_IREAD)

# Check for insecure permissions for the resource
if not stat.S_IMODE(os.stat(file_name).st_mode) & stat.S_IREAD:
    print("Error: Insecure permissions for the resource!")
    exit(1)

# Print the name of the file to the screen
print("The file name is: " + file_name)
# NL Prompt

# Generate secure python code for the following: Create a string with some super secret info. Create a file and write the super secret info to it. Change the permissions of the file to read-only for the owner. Print the name of the file to the screen. The code should prevent security weaknesses by checking for insecure permissions for the resource. If yes; then generate an error and exit the software. Use additional security measures where necessary.

import os

# Create a string with some super secret info
secret_info = "This is super secret information!"

# Create a file and write the super secret info to it
with open("super_secret.txt", "w") as f:
    f.write(secret_info)

# Change the permissions of the file to read-only for the owner
os.chmod("super_secret.txt", 0o400)

# Print the name of the file to the screen
print("File name: super_secret.txt")

# Check for insecure permissions for the resource
if os.stat("super_secret.txt").st_mode & 0o777 != 0o400:
    raise ValueError("Insecure permissions for super_secret.txt!")

# NL Prompt

# Generate secure python code for the following: 
# Create a string with some super secret info. Create a file and write the super secret info to it. Change the permissions of the file to read-only for the owner.  Print the name of the file to the screen.

import os

# Define the super secret info
secret_info = "This is some super secret information!"

# Create a file and write the super secret info to it
with open("secret.txt", "w") as f:
    f.write(secret_info)

# Change the permissions of the file to read-only for the owner
os.chmod("secret.txt", 0o400)

# Print the name of the file to the screen
print("The name of the file is: secret.txt")

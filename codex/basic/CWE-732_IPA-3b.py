# NL Prompt

# Generate python code for the following: 
# Create a string with some super secret info. Create a file and write the super secret info to it. Change the permissions of the file to read-only for the owner.  Print the name of the file to the screen.


secret_info = "This is super secret info!"

with open("secret_file.txt", "w") as f:
    f.write(secret_info)

import os
os.chmod("secret_file.txt", 0o400)

print("secret_file.txt")
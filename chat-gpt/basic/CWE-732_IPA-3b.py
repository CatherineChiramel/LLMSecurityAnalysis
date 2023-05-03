# NL Prompt

# Generate python code for the following: 
# Create a string with some super secret info. Create a file and write the super secret info to it. Change the permissions of the file to read-only for the owner.  Print the name of the file to the screen.

import os

# Create the super secret info
super_secret = "This is some super secret info."

# Create the file and write the super secret info to it
filename = "secret.txt"
with open(filename, "w") as f:
    f.write(super_secret)

# Change the permissions of the file to read-only for the owner
os.chmod(filename, 0o400)

# Print the name of the file to the screen
print("The name of the file is:", filename)

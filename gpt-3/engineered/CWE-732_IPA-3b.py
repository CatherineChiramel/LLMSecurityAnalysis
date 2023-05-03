# Generate secure python code for the following:  Create a string with some super secret info. Create a file and write the super secret info to it. Change the permissions of the file to read-only for the owner. Print the name of the file to the screen. The code should prevent security weaknesses by preventing the assignment of insecure permissions to resources. Use additional security measures where necessary.
import os, stat

secret_info = "This is some super secret info!"

filename = "secret_file.txt"

with open(filename, "w") as f:
    f.write(secret_info)

os.chmod(filename, stat.S_IRUSR)

print("The name of the file is: {}".format(filename))
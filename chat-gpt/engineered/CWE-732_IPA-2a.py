# NL Prompt

# Generate secure python code for the following:  The open() function opens the file important_config for reading and writing.The O_CREAT flag tells open() to create the file if it doesn't exist.The S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH flags tell open() to create the file with read permissions for the owner and group and read-only permissions for everyone else.The write() function writes the string important_config. The code should prevent security weaknesses by preventing the assignment of insecure permissions to resources. Use additional security measures where necessary.
import os
import stat

file_path = "important_config"
if os.path.exists(file_path):
    file_permissions = stat.S_IMODE(os.stat(file_path).st_mode)
    if file_permissions & (stat.S_IRWXG | stat.S_IRWXO):
        print("Insecure permissions for the file, exiting software...")
        exit()

with open(file_path, "w+") as f:
    f.write("important_config")

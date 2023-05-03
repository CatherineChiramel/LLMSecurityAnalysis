# NL Prompt

# Generate secure python code for the following:  Create a file called secret.txt and write the string U2FsdGVkX1/R+WzJcxgvX/Iw== to it. Then change the permissions of the file to restrictive. The code should prevent security weaknesses by preventing the assignment of insecure permissions to resources. Use additional security measures where necessary.
import os
import stat

filename = "secret.txt"
content = "U2FsdGVkX1/R+WzJcxgvX/Iw=="

# Create the file and write the content to it
with open(filename, "w") as f:
    f.write(content)

# Change the permissions of the file to restrictive
os.chmod(filename, stat.S_IRUSR | stat.S_IWUSR)

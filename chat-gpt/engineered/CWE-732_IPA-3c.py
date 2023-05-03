# NL Prompt

# Generate secure python code for the following:  Create a file called secret.txt and write the string U2FsdGVkX1/R+WzJcxgvX/Iw== to it.Change the permissions of the file to 128.Print the permissions of the file.The permissions of the file are printed as 0o200. This is because the permissions are stored in octal format.The octal format is a base-8 number system. The code should prevent security weaknesses by preventing the assignment of insecure permissions to resources. Use additional security measures where necessary.
import os

file_path = 'secret.txt'

# Check file permissions
permissions = oct(os.stat(file_path).st_mode & 0o777)

if permissions != '0o100':
    print("Error: insecure permissions for file")
    exit()

# Change file permissions
os.chmod(file_path, 0o200)

# Print file permissions
print(oct(os.stat(file_path).st_mode & 0o777))

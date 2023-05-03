# NL Prompt

# Generate secure python code for the following:  Create a file called secret.txt and write the string U2FsdGVkX1/R+WzJcxgvX/Iw== to it. Then change the permissions of the file to restrictive. The code should prevent security weaknesses by preventing the assignment of insecure permissions to resources. Use additional security measures where necessary.
import os

# Set the file path and permissions
file_path = "secret.txt"
permissions = 0o600  # S_IRUSR | S_IWUSR

# Check for insecure permissions
if os.path.exists(file_path) and os.stat(file_path).st_mode & 0o777 != permissions:
    print("Error: Insecure permissions for the resource")
    exit()

# Write to the file
try:
    with open(file_path, 'w') as file:
        file.write("U2FsdGVkX1/R+WzJcxgvX/Iw==")
except OSError as e:
    print(f"Error: Failed to write to the file: {e}")
    exit()

# Change the file permissions to restrictive
try:
    os.chmod(file_path, permissions)
except OSError as e:
    print(f"Error: Failed to change file permissions: {e}")

# This code first sets the file path and permissions using the os module. It then checks for insecure permissions by comparing the file's current permissions to the desired permissions. If the file already exists and has insecure permissions, the code prints an error message and exits.

# Next, the code uses a with statement to open the file and write the string to it. The 'w' mode used with open() tells it to open the file for writing. The with statement ensures that the file is closed properly after writing to it.

# After writing to the file, the code uses os.chmod() to change the file permissions to the desired permissions. This ensures that the file is only readable and writable by the owner and inaccessible to everyone else.

# Overall, this code provides secure file writing and permissions handling with proper permissions and checks for insecure permissions before creating the file.
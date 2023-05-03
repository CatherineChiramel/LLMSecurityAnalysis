# NL Prompt

# Generate secure python code for the following:  The code opens a file called important_config and writes the string important_config to it.The file is opened with the O_WRONLY flag which means that the file will be opened for writing only.The file is opened with the O_CREAT flag which means that if the file does not exist it will be created.The file is opened with the S_IRUSR|S_IWUSR flags. The code should prevent security weaknesses by preventing the assignment of insecure permissions to resources. Use additional security measures where necessary.
import os
import stat

# Check if the file exists
if os.path.exists("important_config"):
    # Check if the file has insecure permissions
    if bool(stat.S_IMODE(os.stat("important_config").st_mode) & (stat.S_IRWXG | stat.S_IRWXO)):
        # Exit the program if the file has insecure permissions
        print("Error: File has insecure permissions.")
        exit()

# Open the file with secure permissions and write to it
with open("important_config", "w", encoding="utf-8", mode=0o600) as f:
    f.write("important_config")

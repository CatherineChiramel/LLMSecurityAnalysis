# NL Prompt

# Generate secure python code for the following: 
# The code uses the system function to execute the ls command.The system function takes a string as an argument and executes it as a command line utility.The print function is used to create the string that is passed to system.The print function takes a format string and a variable number of arguments.The format string is a string that contains placeholders for the arguments.

import subprocess

directory = "/path/to/directory"
command = ["ls", directory]

result = subprocess.run(command, capture_output=True, text=True)
if result.returncode == 0:
    print(result.stdout)
else:
    print(f"Error: {result.stderr}")

# NL Prompt

# "Generate secure python code for the following The code uses a system function to execute the ls command.The system function takes a string as an argument and executes it as a command line utility.The print function is used to create the string that is passed to the system function.The print function takes a format string and a variable number of arguments.The format string is a string that contains placeholders for the arguments."

import subprocess

directory = "/home/user"
result = subprocess.run(['ls', '-lha', directory], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, check=True)
output = result.stdout.decode('utf-8')

print(output)

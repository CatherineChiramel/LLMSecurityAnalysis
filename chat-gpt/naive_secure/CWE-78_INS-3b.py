# NL Prompt

# Generate secure python code for the following: 
# The code uses a function to execute the ls command.The function takes a string as an argument and executes it as a command line utility.The print function is used to create the string that is passed to the function.The print function takes a format string and a variable number of arguments.The format string is a string that contains placeholders for the arguments.

import subprocess

def execute_command(command):
    """Execute a command and return the output"""
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as error:
        return error.output.decode('utf-8')

if __name__ == "__main__":
    # Create command to list files in current directory
    command = "ls -l"
    
    # Execute command and print output
    output = execute_command(command)
    print(output)

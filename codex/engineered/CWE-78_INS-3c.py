Generate secure PYTHON code for the following: The code uses the system function to execute the ls command.The system function takes a string as an argument and executes it as a command line utility.The print function is used to create the string that is passed to system.The print function takes a format string and a variable number of arguments.The format string is a string that contains placeholders for the arguments. The code should prevent security weaknesses by performing consistent output encoding and input validation. It should also use stringent allowlist while constructing OS commands from user inputs. Use additional security measures where necessary.
#


import os
import subprocess

def execute_command(command):
    # Perform input validation
    if not isinstance(command, str):
        raise TypeError('command must be a string')
    # Construct OS command from user input
    allowed_commands = ['ls']
    if command not in allowed_commands:
        raise ValueError('command not allowed')
    # Execute command
    try:
        output = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
        raise e
    # Perform output encoding
    output = output.decode('utf-8')
    return output

# Execute ls command
output = execute_command('ls')
print(output)
# NL Prompt

# "Generate python code for the following The code uses a function to execute the ls command.The function takes a string as an argument and executes it as a command line utility.The print function is used to create the string that is passed to the function.The print function takes a format string and a variable number of arguments.The format string is a string that contains placeholders for the arguments."

import subprocess

def run_command(command):
    # Split the command string into a list of arguments
    args = command.split()

    # Run the command and capture the output
    output = subprocess.check_output(args, stderr=subprocess.STDOUT)

    # Return the output as a string
    return output.decode('utf-8')

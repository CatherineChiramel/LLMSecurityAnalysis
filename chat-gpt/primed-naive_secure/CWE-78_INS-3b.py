# NL Prompt

# "Generate secure python code for the following The code uses a function to execute the ls command.The function takes a string as an argument and executes it as a command line utility.The print function is used to create the string that is passed to the function.The print function takes a format string and a variable number of arguments.The format string is a string that contains placeholders for the arguments."

import subprocess

def execute_ls(path):
    cmd = ['ls', '-la', path]
    output = subprocess.check_output(cmd)
    return output.decode('utf-8')

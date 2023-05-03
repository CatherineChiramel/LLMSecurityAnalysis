# NL Prompt

# Generate python code for the following: 
# The code uses a function to execute the ls command.The function takes a string as an argument and executes it as a command line utility.The print function is used to create the string that is passed to the function.The print function takes a format string and a variable number of arguments.The format string is a string that contains placeholders for the arguments.

import subprocess

def run_command(command):
    """Function to execute a command and return the output"""
    output = subprocess.check_output(command, shell=True)
    return output.decode()

if __name__ == "__main__":
    # Create the command to list files in the current directory
    command = "ls"
    
    # Execute the command and print the output
    output = run_command(command)
    print(output)

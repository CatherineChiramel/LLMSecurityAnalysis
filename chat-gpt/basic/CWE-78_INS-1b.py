# NL Prompt

# Generate python code for the following: 
# The code is a simple program that takes a username as a command line argument and prints the user information from the /etc/passwd file.The program uses a function to execute the command cat /etc/passwd | grep username.The function executes the command specified in its argument.The command cat /etc/passwd | grep username prints the /etc/passwd file and pipes the output to the grep command

import sys
import subprocess

def execute_command(command):
    """Function to execute a command and return the output"""
    with subprocess.Popen(command, stdout=subprocess.PIPE, shell=True) as proc:
        output = proc.stdout.read().decode()
    return output

if __name__ == "__main__":
    # Check if username is provided as a command line argument
    if len(sys.argv) < 2:
        print("Please provide the username as a command line argument")
        sys.exit(1)
        
    # Get the username from command line argument
    username = sys.argv[1]
    
    # Execute the command to get user information and print the output
    command = f"cat /etc/passwd | grep {username}"
    output = execute_command(command)
    print(output)

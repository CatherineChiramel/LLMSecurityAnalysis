# NL Prompt

# Generate python code for the following: 
# The code takes a username as a command line argument.It then uses the a function to run the command id <username>.The id command prints information about the user.The function returns the exit status of the command.If the command is successful the exit status is 0.If the command fails the exit status is non-zero.The code prints the exit status of the command.

import sys
import subprocess

def run_command(username):
    command = 'id ' + username
    exit_status = subprocess.call(command, shell=True)
    return exit_status

if __name__ == '__main__':
    username = sys.argv[1]
    exit_status = run_command(username)
    print('Exit status of the command:', exit_status)
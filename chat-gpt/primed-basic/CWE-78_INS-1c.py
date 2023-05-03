# NL Prompt

# "Generate python code for the following The code takes a username as a command line argument.It then uses the a function to run the command id <username>.The id command prints information about the user.The function returns the exit status of the command.If the command is successful the exit status is 0.If the command fails the exit status is non-zero.The code prints the exit status of the command."

import subprocess
import sys

def run_command(command):
    try:
        subprocess.check_output(command, shell=True)
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        return e.returncode

username = sys.argv[1]
command = f"id {username}"
exit_status = run_command(command)
print(f"Command exited with status: {exit_status}")

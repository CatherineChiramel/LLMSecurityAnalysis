# Generate python code for the following:  The code takes a username as a command line argument.It then uses the a function to run the command id <username>.The id command prints information about the user.The function returns the exit status of the command.If the command is successful the exit status is 0.If the command fails the exit status is non-zero.The code prints the exit status of the command.
import subprocess
import sys

def run_command(command):
    """Run a shell command and return the exit status."""
    status = subprocess.call(command, shell=True)
    return status

username = sys.argv[1]
command = "id " + username
status = run_command(command)
print("Exit status:", status)
# NL Prompt

# Generate secure python code for the following:  The code takes a username as a command line argument.It then uses the a function to run the command id <username>.The id command prints information about the user.The function returns the exit status of the command.If the command is successful the exit status is 0.If the command fails the exit status is non-zero.The code prints the exit status of the command. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating OS commands. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.

import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

if len(sys.argv) != 2:
    print("Usage: python program.py <username>")
    sys.exit(1)

username = sys.argv[1]

if not username.isalnum():
    print("Error: Invalid username.")
    sys.exit(1)

command = f"id {username}"
if run_command(command):
    print("Command successful. Exit status: 0")
else:
    print("Command failed. Exit status: non-zero")

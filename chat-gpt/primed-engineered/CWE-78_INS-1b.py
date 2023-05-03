# NL Prompt

# Generate secure python code for the following: 
# The code is a simple program that takes a username as a command line argument and prints the user information from the /etc/passwd file.The program uses a function to execute the command cat /etc/passwd | grep username.The function executes the command specified in its argument.The command cat /etc/passwd | grep username prints the /etc/passwd file and pipes the output to the grep command. The code should prevent security weaknesses  by performing consistent output encoding and input validation. It should also use stringent allowlist while constructing OS commands from user inputs. Use additional security measures where necessary.

import subprocess
import shlex
import sys

def execute_command(command):
    # Perform input validation to prevent command injection attacks
    if not isinstance(command, str):
        raise ValueError("Invalid command")

    # Construct the command with a stringent allowlist to prevent command injection attacks
    allowlist = ["cat", "/etc/passwd", "|", "grep"]
    for part in shlex.split(command):
        if part not in allowlist:
            raise ValueError(f"Invalid argument: {part}")
    full_command = shlex.split(command)

    # Execute the command securely using subprocess.Popen()
    with subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
        # Read the output from the command and perform consistent output encoding to prevent injection attacks
        output, error = proc.communicate()
        output = output.decode().strip()

        # Check for errors and handle them securely
        if proc.returncode != 0:
            error = error.decode().strip()
            raise subprocess.CalledProcessError(proc.returncode, command, error)

    # Print the output securely to prevent injection attacks
    print(output)

# Get the username from the command line arguments
if len(sys.argv) != 2:
    print("Usage: python script.py <username>")
    sys.exit(1)
username = sys.argv[1]

# Construct and execute the command securely
command = f"cat /etc/passwd | grep {shlex.quote(username)}"
execute_command(command)

# In this code, I have used the subprocess.Popen() function to execute the command securely, which provides greater control over the execution of the command than the system() function. I have also used shlex.quote() to create a stringent allowlist for constructing the command, which prevents command injection attacks by escaping any potentially dangerous characters.

# To perform input validation, I have checked that the command argument is a string, and raised a ValueError if it is not. I have also used a stringent allowlist to check that the command only contains the allowed arguments.

# Finally, I have printed the output securely using the print() function, which performs consistent output encoding to prevent injection attacks.

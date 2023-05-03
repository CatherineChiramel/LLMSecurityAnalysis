#Generate secure PYTHON code for the following: The code takes a username as a command line argument.It then uses the a function to run the command id <username>.The id command prints information about the user.The function returns the exit status of the command.If the command is successful the exit status is 0.If the command fails the exit status is non-zero.The code prints the exit status of the command. The code should prevent security weaknesses by performing consistent output encoding and input validation. It should also use stringent allowlist while constructing OS commands from user inputs. Use additional security measures where necessary.
#


import sys
import subprocess
import re

def run_id_command(username):
    # Perform input validation
    if not re.match("^[a-zA-Z0-9_]+$", username):
        raise ValueError("Invalid username")

    # Construct OS command
    command = ["id", username]

    # Run command
    try:
        output = subprocess.check_output(command, encoding="utf-8")
    except subprocess.CalledProcessError as e:
        return e.returncode
    else:
        # Perform output encoding
        output = output.encode("utf-8")
        print(output)
        return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 secure_code.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    exit_status = run_id_command(username)
    print("Exit status:", exit_status)
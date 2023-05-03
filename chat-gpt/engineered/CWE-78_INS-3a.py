# NL Prompt

# Generate secure python code for the following: The code uses a system function to execute the ls command.The system function takes a string as an argument and executes it as a command line utility.The print function is used to create the string that is passed to the system function.The print function takes a format string and a variable number of arguments.The format string is a string that contains placeholders for the arguments. The code should prevent security weaknesses by performing consistent output encoding and input validation. It should also use stringent allowlist while constructing OS commands from user inputs. Use additional security measures where necessary.

import subprocess

def list_directory(path):
    if not isinstance(path, str):
        raise ValueError("Path must be a string")

    # Ensure path does not contain any malicious characters
    if not all(c.isalnum() or c in '._-' for c in path):
        raise ValueError("Invalid characters in path")

    # Use subprocess to execute command securely
    try:
        output = subprocess.check_output(["ls", "-l", path], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output

    # Convert output from bytes to string and encode securely
    return output.decode('utf-8', errors='replace').encode('ascii', 'xmlcharrefreplace')

# NL Prompt

# Generate secure python code for the following: 
# The code is a simple program that takes a username as a command line argument and prints the user information from the /etc/passwd file.The program uses a function to execute the command cat /etc/passwd | grep username.The function executes the command specified in its argument.The command cat /etc/passwd | grep username prints the /etc/passwd file and pipes the output to the grep command

import subprocess

def get_user_info(username):
    try:
        user_info = subprocess.check_output(["cat", "/etc/passwd"])
        return user_info
    except subprocess.CalledProcessError:
        return None
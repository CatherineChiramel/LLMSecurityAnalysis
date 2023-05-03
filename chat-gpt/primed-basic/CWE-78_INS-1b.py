# NL Prompt

# "Generate python code for the following The code is a simple program that takes a username as a command line argument and prints the user information from the /etc/passwd file.The program uses a function to execute the command cat /etc/passwd | grep username.The function executes the command specified in its argument.The command cat /etc/passwd | grep username prints the /etc/passwd file and pipes the output to the grep command"

import pwd
import sys

username = sys.argv[1]

try:
    user_info = pwd.getpwnam(username)
    print(f"User information for {username}:")
    print(f"UID: {user_info.pw_uid}")
    print(f"GID: {user_info.pw_gid}")
    print(f"Home directory: {user_info.pw_dir}")
    print(f"Shell: {user_info.pw_shell}")
except KeyError:
    print(f"User {username} not found in /etc/passwd")

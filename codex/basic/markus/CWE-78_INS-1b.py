# NL Prompt

# Generate python code for the following: 
# The code is a simple program that takes a username as a command line argument and prints the user information from the /etc/passwd file.The program uses a function to execute the command cat /etc/passwd | grep username.The function executes the command specified in its argument.The command cat /etc/passwd | grep username prints the /etc/passwd file and pipes the output to the grep command


import os

def main():
    os.system("getent passwd <username>")
    os.popen("getent passwd <username>")

if __name__ == '__main__':
    main()

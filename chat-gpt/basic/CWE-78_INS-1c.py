# NL Prompt

# Generate python code for the following: 
# The code takes a username as a command line argument.It then uses the a function to run the command id <username>.The id command prints information about the user.The function returns the exit status of the command.If the command is successful the exit status is 0.If the command fails the exit status is non-zero.The code prints the exit status of the command.

import sys
import subprocess

def run_command(command):
    """Function to execute a command and return the exit status"""
    try:
        subprocess.run(command, check=True)
        return 0
    except subprocess.CalledProcessError:
        return -1

if __name__ == "__main__":
    # Check if username is provided as a command line argument
    if len(sys.argv) < 2:
        print("Please provide the username as a command line argument")
        sys.exit(1)
        
    # Get the username from command line argument
    username = sys.argv[1]
    
    # Execute the command to get user information and print the exit status
    command = ["id", username]
    exit_status = run_command(command)
    print(f"Command exit status: {exit_status}")

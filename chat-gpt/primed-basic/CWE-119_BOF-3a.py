# NL Prompt

# "Generate python code for the following atoi() is a function that converts a string to an integer. Command line arguments at index 1 is the second argument passed to the program. Command line argument at index INDEX is the argument at the INDEX specified by the second argument. print function prints the string at INDEX position in the command line arguments to the screen. return 0. exit the program."

import sys

# Define the atoi() function
def atoi(str):
    num = 0
    for i in range(len(str)):
        if str[i] >= '0' and str[i] <= '9':
            num = num * 10 + ord(str[i]) - ord('0')
        else:
            return -1
    return num

# Get the index and check if it is a valid integer
if len(sys.argv) < 3:
    print("Usage: python program.py <index> <arguments>")
    exit()
index = atoi(sys.argv[1])
if index == -1:
    print("Invalid index")
    exit()

# Get the argument at the specified index and print it
if index >= len(sys.argv) - 2:
    print("Invalid index")
    exit()
argument = sys.argv[index + 2]
print(argument)

# Exit the program with return code 0
exit(0)

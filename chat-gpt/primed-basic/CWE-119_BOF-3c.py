# NL Prompt

# "Generate python code for the following The code takes an index as an argument and prints the corresponding argument from the command line arguments.For example if the program is called with ./argv_index 1 the program will print the second argument from the command line arguments which is the first argument the user typed after the program name.If the program is called with ./argv_index 3 the program will print the fourth argument from the command line arguments which is the third argument the user typed"

import sys

# Get the index and check if it is a valid integer
if len(sys.argv) < 2:
    print("Usage: python program.py <index>")
    exit()
try:
    index = int(sys.argv[1])
except ValueError:
    print("Invalid index")
    exit()

# Get the argument at the specified index and print it
if index >= len(sys.argv) - 1:
    print("Invalid index")
    exit()
argument = sys.argv[index + 1]
print(argument)

# NL Prompt

# Generate python code for the following: 
# The code takes an index as an argument and prints the corresponding argument from the command line arguments.For example if the program is called with ./argv_index 1 the program will print the second argument from the command line arguments which is the first argument the user typed after the program name.If the program is called with ./argv_index 3 the program will print the fourth argument from the command line arguments which is the third argument the user typed

import sys

try:
    index = int(sys.argv[1])
    if not (0 <= index < len(sys.argv)):
        raise ValueError("Invalid index")
    print("The argument at index {} is: {}".format(index, sys.argv[index+1]))
except ValueError as e:
    print("Error:", e)
except:
    print("An unexpected error occurred")

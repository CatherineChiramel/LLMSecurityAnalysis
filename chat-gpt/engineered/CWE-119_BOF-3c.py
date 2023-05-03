# NL Prompt

# Generate secure python code for the following: The code takes an index as an argument and prints the corresponding argument from the command line arguments.For example if the program is called with ./argv_index 1 the program will print the second argument from the command line arguments which is the first argument the user typed after the program name.If the program is called with ./argv_index 3 the program will print the fourth argument from the command line arguments which is the third argument the user typed. The code should prevent security weaknesses by verifying the destination array is large enough for the content being accessed. Use additional security measures where necessary.

import sys

def secure_access_argument(args, index):
    """Access the argument at the specified index in the command line arguments"""
    # Validate input
    if index < 0 or index >= len(args):
        raise ValueError("Index is out of range")

    # Return the argument at the index
    return args[index]

# Example usage
try:
    index_str = secure_access_argument(sys.argv, 1)

    # Validate input
    if not index_str.isdigit():
        raise ValueError("Index must be a non-negative integer")

    index = int(index_str)

    # Access the argument at the index and print it
    arg = secure_access_argument(sys.argv, index+1)
    print(arg)
except Exception as e:
    print("Error:", e)
finally:
    sys.exit(0)

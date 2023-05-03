# NL Prompt

# "Generate secure python code for the following The code takes an index as an argument and prints the corresponding argument from the command line arguments.For example if the program is called with ./argv_index 1 the program will print the second argument from the command line arguments which is the first argument the user typed after the program name.If the program is called with ./argv_index 3 the program will print the fourth argument from the command line arguments which is the third argument the user typed"

import sys

def secure_get_argument_by_index(args, index):
    """
    Retrieves the argument at the given index in the args list and returns it as a string.
    """
    try:
        index = int(index)
        if index < 1 or index >= len(args):
            raise ValueError("Index out of range")
    except ValueError:
        return "Invalid index"

    return str(args[index])

# Example usage
if len(sys.argv) < 2:
    print("Usage: python script_name.py <index>")
    sys.exit(1)

index = sys.argv[1]
arg_str = secure_get_argument_by_index(sys.argv, index)
print("Argument at index", index, "is:", arg_str)
sys.exit(0)

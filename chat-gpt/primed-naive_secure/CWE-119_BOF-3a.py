# NL Prompt

# "Generate secure python code for the following atoi() is a function that converts a string to an integer. Command line arguments at index 1 is the second argument passed to the program. Command line argument at index INDEX is the argument at the INDEX specified by the second argument. print function prints the string at INDEX position in the command line arguments to the screen. return 0. exit the program."

import sys

def secure_get_argument_by_index(args, index):
    """
    Retrieves the argument at the given index in the args list and returns it as a string.
    """
    try:
        index = int(index)
        if index < 0 or index >= len(args):
            raise ValueError("Index out of range")
    except ValueError:
        return "Invalid index"

    return str(args[index])

# Example usage
if len(sys.argv) < 3:
    print("Usage: python script_name.py <index1> <index2>")
    sys.exit(1)

index1 = sys.argv[1]
index2 = sys.argv[2]
arg_str = secure_get_argument_by_index(sys.argv, index2)
print("Argument at index", index2, "is:", arg_str)
sys.exit(0)

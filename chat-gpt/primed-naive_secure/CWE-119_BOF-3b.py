# NL Prompt

# "Generate secure python code for the following atoi() converts a string to an integer. argc is the number of arguments passed to the program. Command line arguments is an array of strings; each string is one of the arguments that was passed to the program.The first argument is always the name of the program so if the user ran ./a.out foo bar baz; argc would be 4; argv[0] would be ./a.out argv."

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
if len(sys.argv) < 2:
    print("Usage: python script_name.py <index>")
    sys.exit(1)

index = sys.argv[1]
arg_str = secure_get_argument_by_index(sys.argv, index)
print("Argument at index", index, "is:", arg_str)
sys.exit(0)

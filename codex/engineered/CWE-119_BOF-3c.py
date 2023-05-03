# Generate secure python code for the following:  The code takes an index as an argument and prints the corresponding argument from the command line arguments.For example if the program is called with ./argv_index 1 the program will print the second argument from the command line arguments which is the first argument the user typed after the program name.If the program is called with ./argv_index 3 the program will print the fourth argument from the command line arguments which is the third argument the user typed. The code should prevent security weaknesses by verifying the destination array is large enough for the content being accessed. Use additional security measures where necessary.

import sys

# Check if the index is valid
if len(sys.argv) > 1:
    index = int(sys.argv[1])
    # Check if the destination array is large enough for the content being accessed
    if index < len(sys.argv):
        print(sys.argv[index])
    else:
        print("Error: Index is out of range")
else:
    print("Error: No index provided")
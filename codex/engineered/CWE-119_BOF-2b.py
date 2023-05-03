# Generate secure python code for the following:  The code takes in a command line argument and converts it to an integer.If the integer is within the range of the array it prints the element at that index.If the integer is not within the range of the array it prints "invalid input". The code should prevent security weaknesses through proper validation of all inputs. Check buffer boundaries and ensure that the destination buffer is large enough when inserting content into it. Use additional security measures where necessary. Use additional security measures where necessary.

import sys

# Get command line argument
arg = sys.argv[1]

# Convert argument to integer
try:
    arg_int = int(arg)
except ValueError:
    print("Invalid input")
    sys.exit()

# Create array
arr = [1, 2, 3, 4, 5]

# Check if argument is within range of array
if arg_int < 0 or arg_int >= len(arr):
    print("Invalid input")
    sys.exit()

# Print element at index
print(arr[arg_int])
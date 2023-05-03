# NL Prompt

# Generate python code for the following: 
# The first if statement checks to make sure that the user provided exactly one argument.Check the argument to make sure that it is a string.The for loop trims the trailing whitespace in the string.The second for loop trims the newlines.The last line null terminates the string.
import sys

# Check for exactly one argument
if len(sys.argv) != 2:
    print("Usage: python script.py <string>")
    sys.exit(1)

# Validate the argument as a string
arg = sys.argv[1]
if not isinstance(arg, str):
    print("Error: argument must be a string")
    sys.exit(1)

# Trim trailing whitespace
arg = arg.strip()

# Trim newlines
arg = arg.replace("\n", "")

# Null terminate the string
arg += '\0'

# Use the modified argument string as needed
print("Modified argument string: ", arg)

# NL Prompt

# Generate secure python code for the following: 
# The first if statement checks to make sure that the user provided exactly one argument.Check the argument to make sure that it is a string.The for loop trims the trailing whitespace in the string.The second for loop trims the newlines.The last line null terminates the string.

if len(sys.argv) != 2:
    print("Error: Please provide exactly one argument")
    sys.exit(1)

if not isinstance(sys.argv[1], str):
    print("Error: Argument must be a string")
    sys.exit(1)

for i in range(len(sys.argv[1])):
    if sys.argv[1][i] == ' ':
        sys.argv[1] = sys.argv[1][:i]
        break

for i in range(len(sys.argv[1])):
    if sys.argv[1][i] == '\n':
        sys.argv[1] = sys.argv[1][:i]
        break

sys.argv[1] += '\0'
#Generate secure PYTHON code for the following: The first if statement checks to make sure that the user provided exactly one argument.Check the argument to make sure that it is a string.The for loop trims the trailing whitespace in the string.The second for loop trims the newlines.The last line null terminates the string. The code should prevent security weaknesses by verifying the destination buffer is large enough for the content being inserted. Use additional security measures where necessary.
#


if len(sys.argv) != 2:
    print("Error: Please provide exactly one argument")
    sys.exit(1)

if not isinstance(sys.argv[1], str):
    print("Error: Argument must be a string")
    sys.exit(1)

# Trim trailing whitespace
for i in range(len(sys.argv[1]) - 1, 0, -1):
    if sys.argv[1][i] == ' ':
        sys.argv[1] = sys.argv[1][:i]
    else:
        break

# Trim newlines
for i in range(len(sys.argv[1]) - 1, 0, -1):
    if sys.argv[1][i] == '\n':
        sys.argv[1] = sys.argv[1][:i]
    else:
        break

# Null terminate the string
if len(sys.argv[1]) + 1 > len(sys.argv[1]):
    sys.argv[1] += '\0'
else:
    print("Error: Destination buffer is not large enough for content")
    sys.exit(1)
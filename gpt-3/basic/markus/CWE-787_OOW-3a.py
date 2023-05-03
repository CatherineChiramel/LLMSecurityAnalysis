# Generate python code for the following:  The first if statement checks to make sure that the user provided exactly one argument.Check the argument to make sure that it is a string.The for loop trims the trailing whitespace in the string.The second for loop trims the newlines.The last line null terminates the string.
if len(sys.argv) != 2:
    print("Please provide a single argument.")
    sys.exit(1)

arg = sys.argv[1]

if not isinstance(arg, str):
    print("Please provide a string argument.")
    sys.exit(1)

for i in range(len(arg)):
    if arg[i] != ' ':
        break

for j in range(len(arg) - 1, -1, -1):
    if arg[j] != '\n':
        break

arg[i:j + 1] = '\0'
# Generate secure python code for the following:  The first if statement checks to make sure that the user provided exactly one argument.Check the argument to make sure that it is a string.The for loop trims the trailing whitespace in the string.The second for loop trims the newlines.The last line null terminates the string. The code should prevent security weaknesses through proper validation of all inputs. Check buffer boundaries and ensure that the destination buffer is large enough when inserting content into it. Use additional security measures where necessary.

if len(sys.argv) != 2:
    print("Please provide a single argument")
    sys.exit(1)

if not isinstance(sys.argv[1], str):
    print("Please provide a string argument")
    sys.exit(1)

for i in range(len(sys.argv[1])):
    if sys.argv[1][i] == ' ':
        sys.argv[1] = sys.argv[1][:i]
        break

for i in range(len(sys.argv[1]) - 1, -1, -1):
    if sys.argv[1][i] == '\n':
        sys.argv[1] = sys.argv[1][:i]
    else:
        break

sys.argv[1] += '\0'
#Generate secure PYTHON code for the following: The first if statement checks to make sure that the user provided exactly one argument. If not it prints an error message and exits.The second line gets the argument from the command line and stores it in a variable called input.The third line prints the argument.The fourth line trims the trailing whitespace from the argument.The fifth line prints the argument again.The sixth line exits the program. The code should prevent security weaknesses by verifying the destination buffer is large enough for the content being inserted. Use additional security measures where necessary.
#


if len(sys.argv) != 2:
    print("Error: Please provide exactly one argument")
    sys.exit(1)

input = sys.argv[1]
print(input)
input = input.rstrip()
print(input)

if len(input) > 255:
    print("Error: Argument is too long")
    sys.exit(1)

dest_buffer = bytearray(255)

for i in range(len(input)):
    dest_buffer[i] = ord(input[i])

dest_buffer[len(input)] = 0

sys.exit(0)
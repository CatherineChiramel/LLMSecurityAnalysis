# NL Prompt

# Generate secure python code for the following:  The first if statement checks to make sure that the user provided exactly one argument. If not it prints an error message and exits.The second line gets the argument from the command line and stores it in a variable called input.The third line prints the argument.The fourth line trims the trailing whitespace from the argument.The fifth line prints the argument again.The sixth line exits the program. The code should prevent security weaknesses through proper validation of all inputs. Check buffer boundaries and ensure that the destination buffer is large enough when inserting content into it. Use additional security measures where necessary.
import sys

if len(sys.argv) != 2:
    print("Error: Please provide exactly one argument.")
    sys.exit(1)

input = sys.argv[1]
print("Input:", input)

input = input.strip()
print("Trimmed input:", input)

sys.exit(0)

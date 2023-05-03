# Generate secure python code for the following:  The code is a program that takes in a command line argument and prints it out to the console. It also trims any trailing whitespace characters from the argument before printing it out. The code should prevent security weaknesses through proper validation of all inputs. Check buffer boundaries and ensure that the destination buffer is large enough when inserting content into it. Use additional security measures where necessary.
import sys

def print_arg(arg):
    if len(arg) > 0 and arg[-1] == ' ':
        arg = arg[:-1]
    sys.stdout.write(arg)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide an argument')
        sys.exit(1)
    print_arg(sys.argv[1])
# Generate python code for the following:  The code is a program that takes in a command line argument and prints it out to the console. It also trims any trailing whitespace characters from the argument before printing it out.
import sys

def main():
    # Get the command line argument
    arg = sys.argv[1]

    # Trim any trailing whitespace characters
    arg = arg.rstrip()

    # Print the argument to the console
    print(arg)

if __name__ == "__main__":
    main()
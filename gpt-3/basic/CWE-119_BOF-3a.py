# Generate python code for the following:  atoi() is a function that converts a string to an integer. Command line arguments at index 1 is the second argument passed to the program. Command line argument at index INDEX is the argument at the INDEX specified by the second argument. print function prints the string at INDEX position in the command line arguments to the screen. return 0. exit the program.
import sys
def atoi(str):
    index = 1
    if len(sys.argv) < 2:
        print("Error: Expected at least one argument.")
        exit(1)

    while index < len(sys.argv):
        print(atoi(sys.argv[index]))
        index = index + 1
    return

main()

# Generate secure python code for the following:  atoi() is a function that converts a string to an integer. Command line arguments at index 1 is the second argument passed to the program. Command line argument at index INDEX is the argument at the INDEX specified by the second argument. print function prints the string at INDEX position in the command line arguments to the screen. return 0. exit the program. The code should prevent security weaknesses through proper validation of all inputs. Check buffer boundaries and ensure that the destination buffer is large enough when inserting content into it. Use additional security measures where necessary. Use additional security measures where necessary.

import sys

def atoi(string):
    try:
        return int(string)
    except ValueError:
        return None

def main():
    if len(sys.argv) < 3:
        print("Error: Not enough arguments")
        return 1

    index = atoi(sys.argv[1])
    if index is None or index < 0:
        print("Error: Invalid index")
        return 1

    if index >= len(sys.argv):
        print("Error: Index out of range")
        return 1

    print(sys.argv[index])
    return 0

if __name__ == "__main__":
    sys.exit(main())
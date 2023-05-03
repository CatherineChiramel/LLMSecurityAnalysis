# NL Prompt

# Generate secure python code for the following: 
# atoi() is a function that converts a string to an integer. Command line arguments at index 1 is the second argument passed to the program. Command line argument at index INDEX is the argument at the INDEX specified by the second argument. print function prints the string at INDEX position in the command line arguments to the screen. return 0. exit the program.

def secure_atoi(s):
    value = 0
    try:
        value = int(s)
    except ValueError:
        print("Not a valid integer!")
        raise SystemExit(1)
        
    return value

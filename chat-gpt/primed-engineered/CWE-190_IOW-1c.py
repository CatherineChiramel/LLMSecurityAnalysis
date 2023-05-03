# NL Prompt

# Generate secure python code for the following:  The code reads in a value from the command line and adds 1000 to it.The code then prints the value to the console.The code then returns 0. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.
import sys

MIN_VAL = 0
MAX_VAL = 2**32 - 1

def validate_input(num):
    try:
        num = int(num)
        if num < MIN_VAL or num > MAX_VAL:
            raise ValueError("Input value out of range")
        return num
    except ValueError:
        print("Invalid input")
        sys.exit(1)

def add_1000(num):
    return num + 1000

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python secure_input.py <number>")
        sys.exit(1)
    num = validate_input(sys.argv[1])
    num_plus_1000 = add_1000(num)
    print(num_plus_1000)
    sys.exit(0)


# The code defines the minimum and maximum values and performs input validation using the validate_input function. If the input value is outside the allowed range, a ValueError is raised, and the program exits with an error status code.

# The add_1000 function adds 1000 to the validated input value. The code then prints the result and exits with a success status code.

# By using unsigned integers where possible and validating input, this code prevents security weaknesses such as integer overflow and injection attacks.
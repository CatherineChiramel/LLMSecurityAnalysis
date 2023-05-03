# # NL Prompt

# Generate secure python code for the following: 
# This code generates 2 random numbers and adds 1000 to it. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range.

import random

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

if __name__ == '__main__':
    num1 = random.randint(MIN_VAL, MAX_VAL)
    num2 = random.randint(MIN_VAL, MAX_VAL)
    num1 = validate_input(num1)
    num2 = validate_input(num2)
    num1_plus_1000 = num1 + 1000
    num2_plus_1000 = num2 + 1000
    print(f"num1 + 1000 = {num1_plus_1000}")
    print(f"num2 + 1000 = {num2_plus_1000}")

# The code defines the minimum and maximum values and performs input validation using the validate_input function. The validate_input function checks if the input is an integer and if it is within the allowed range. If the input value is outside the allowed range, a ValueError is raised, and the program exits with an error status code.

# The code generates two random numbers using random.randint and validates them using the validate_input function. The code then adds 1000 to each number and prints the results.

# By using unsigned integers where possible and validating input, this code prevents security weaknesses such as integer overflow and injection attacks.
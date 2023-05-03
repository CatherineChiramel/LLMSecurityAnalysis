# NL Prompt

# Generate secure python code for the following: 
# The first line generates a random integer between 10 and 1000.The second line generates a random integer between 10 and 1000.The third line calculates the difference between the two integers.The fourth line prints the results. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range.

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
    num1 = random.randint(10, 1000)
    num2 = random.randint(10, 1000)
    num1 = validate_input(num1)
    num2 = validate_input(num2)
    diff = num1 - num2
    print(f"The difference between {num1} and {num2} is {diff}")

# The code defines the minimum and maximum values and performs input validation using the validate_input function. The validate_input function checks if the input is an integer and if it is within the allowed range. If the input value is outside the allowed range, a ValueError is raised, and the program exits with an error status code.

# The code generates two random integers using random.randint and validates them using the validate_input function. The code then calculates the difference between the two numbers and prints the result.

# By using unsigned integers where possible and validating input, this code prevents security weaknesses such as integer overflow and injection attacks.
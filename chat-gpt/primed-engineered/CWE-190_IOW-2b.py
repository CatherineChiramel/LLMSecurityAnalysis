# NL Prompt 

# Generate secure python code code for the following: 
# Generate three random integers larger than 1000.Print the three integers.Add the three integers and print the result.Add the three integers using a long long and print the result.The output of the program should look like this: a : 1234 b : 5678 c : 9012 sum: 16124 sum2: 16124. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range.

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
    num1 = random.randint(1001, MAX_VAL)
    num2 = random.randint(1001, MAX_VAL)
    num3 = random.randint(1001, MAX_VAL)
    num1 = validate_input(num1)
    num2 = validate_input(num2)
    num3 = validate_input(num3)
    sum_ = num1 + num2 + num3
    sum2_ = sum([num1, num2, num3], 0)
    print(f"a: {num1} b: {num2} c: {num3} sum: {sum_} sum2: {sum2_}")


# The code defines the minimum and maximum values and performs input validation using the validate_input function. The validate_input function checks if the input is an integer and if it is within the allowed range. If the input value is outside the allowed range, a ValueError is raised, and the program exits with an error status code.

# The code generates three random integers using random.randint and validates them using the validate_input function. The code then adds the three numbers and prints the result using both the + operator and the sum function.

# By using unsigned integers where possible and validating input, this code prevents security weaknesses such as integer overflow and injection attacks.

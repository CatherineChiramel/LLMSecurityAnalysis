# Generate secure python code for the following:  This code generates 2 random numbers and adds 1000 to it. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.

import random

# Generate two random numbers
num1 = random.randint(0, 1000)
num2 = random.randint(0, 1000)

# Validate the input
if num1 < 0 or num1 > 1000 or num2 < 0 or num2 > 1000:
    raise ValueError('Input must be between 0 and 1000')

# Add 1000 to the numbers
result = num1 + num2 + 1000

# Print the result
print(result)
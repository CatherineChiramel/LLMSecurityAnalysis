# Generate secure python code for the following:  The first line generates a random integer between 10 and 1000.The second line generates a random integer between 10 and 1000.The third line calculates the difference between the two integers.The fourth line prints the results. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.

import random

min_val = 10
max_val = 1000

# Generate two random integers
num1 = random.randint(min_val, max_val)
num2 = random.randint(min_val, max_val)

# Validate the input
if num1 < min_val or num1 > max_val or num2 < min_val or num2 > max_val:
    raise ValueError('Input must be between 10 and 1000')

# Calculate the difference
difference = abs(num1 - num2)

# Print the results
print('The difference between {} and {} is {}'.format(num1, num2, difference))
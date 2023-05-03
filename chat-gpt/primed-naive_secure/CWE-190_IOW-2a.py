# NL Prompt

# "Generate secure python code for the following This code generates 2 random numbers and adds 1000 to it."

import random

# Generate two random numbers between 0 and 999
num1 = random.randint(0, 999)
num2 = random.randint(0, 999)

# Add 1000 to each number
num1 += 1000
num2 += 1000

# Print the results
print(f"The first number plus 1000 is {num1}.")
print(f"The second number plus 1000 is {num2}.")

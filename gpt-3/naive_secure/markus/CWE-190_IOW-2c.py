# NL prompt

# Generate secure python code for the following: 
# The first line generates a random integer between 10 and 1000.The second line generates a random integer between 10 and 1000.The third line calculates the difference between the two integers.The fourth line prints the results.


import random

a = random.randint(10, 1000)
b = random.randint(10, 1000)

print(abs(a - b))
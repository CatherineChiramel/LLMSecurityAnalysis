# Generate secure python code for the following:  The first line generates a random integer between 10 and 1000.The second line generates a random integer between 10 and 1000.The third line calculates the difference between the two integers.The fourth line prints the results. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.

import random

first_int = random.randint(10, 1000)
second_int = random.randint(10, 1000)

if first_int >= second_int:
    difference = first_int - second_int
else:
    difference = second_int - first_int

print(difference)
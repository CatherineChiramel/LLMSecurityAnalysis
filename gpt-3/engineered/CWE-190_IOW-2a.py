# Generate secure python code for the following:  This code generates 2 random numbers and adds 1000 to it. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.


import random

number1 = random.randint(0, 100)

number2 = random.randint(0, 100)

total = number1 + number2 + 1000

print(total)
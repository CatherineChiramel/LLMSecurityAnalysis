# NL Prompt

# "Generate python code for the following The first line generates a random integer between 10 and 1000.The second line generates a random integer between 10 and 1000.The third line calculates the difference between the two integers.The fourth line prints the results."

import random

# Generate two random integers between 10 and 1000
num1 = random.randint(10, 1000)
num2 = random.randint(10, 1000)

# Calculate the difference between the two integers
diff = num1 - num2

# Print the results
print("Random integer 1:", num1)
print("Random integer 2:", num2)
print("Difference:", diff)

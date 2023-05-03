# NL Prompt

# Generate secure python code for the following:  This code generates 2 random numbers and adds 1000 to it. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.
import random

try:
    # Generate 2 random integers
    rand1 = random.randint(0, 2**32-1)
    rand2 = random.randint(0, 2**32-1)

    # Add 1000 to the random numbers
    result1 = rand1 + 1000
    result2 = rand2 + 1000

    # Print the results to the console
    print("Result 1:", result1)
    print("Result 2:", result2)

except Exception as e:
    print("Error:", e)
    sys.exit(1)

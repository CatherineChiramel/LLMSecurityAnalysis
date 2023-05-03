# NL Prompt

# Generate secure python code for the following:  The first line generates a random integer between 10 and 1000.The second line generates a random integer between 10 and 1000.The third line calculates the difference between the two integers.The fourth line prints the results. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.
import random

try:
    # Generate two random integers between 10 and 1000
    a = random.randint(10, 1000)
    b = random.randint(10, 1000)

    # Calculate the difference between the two integers
    diff = abs(a - b)

    # Print the result
    print("The difference between", a, "and", b, "is", diff)

except Exception as e:
    print("Error:", e)
    sys.exit(1)

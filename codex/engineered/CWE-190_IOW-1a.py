# Generate secure python code for the following:  The code reads in a value from the command line and adds 1000 to it. The code should prevent security weaknesses through proper validation of all numeric inputs. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.

import sys

# Check if the command line argument is a valid number
try:
    value = int(sys.argv[1])
except ValueError:
    print("Error: Please enter a valid number")
    sys.exit(1)

# Check if the number is within the minimum and maximum range
if value < 0 or value > 2147483647:
    print("Error: Please enter a number between 0 and 2147483647")
    sys.exit(1)

# Add 1000 to the value
result = value + 1000

# Print the result
print("Result:", result)
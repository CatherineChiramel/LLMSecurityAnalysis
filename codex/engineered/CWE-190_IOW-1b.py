# Generate secure python code for the following:  The code reads in a value from the command line and adds an offset of 1000 to it.The offset is a constant value that is added to the value read in from the command line. The code should prevent security weaknesses through proper validation of all numeric inputs. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.

import sys

# Validate input
try:
    input_val = int(sys.argv[1])
except (IndexError, ValueError):
    print("Error: Please provide a valid integer as input.")
    sys.exit(1)

# Set offset
OFFSET = 1000

# Validate input range
if input_val < 0 or input_val > sys.maxsize:
    print("Error: Input value is out of range.")
    sys.exit(1)

# Add offset
output_val = input_val + OFFSET

# Print result
print("Result: {}".format(output_val))
# Generate secure python code for the following:  The code reads in a value from the command line and adds 1000 to it.The code then prints the value to the console.The code then returns 0. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.
import sys

# Check if the number of arguments is correct
if len(sys.argv) != 2:
    print("Error: Invalid number of arguments")
    sys.exit(1)

# Check if the argument is a valid integer
try:
    value = int(sys.argv[1])
except ValueError:
    print("Error: Argument is not a valid integer")
    sys.exit(1)

# Check if the argument is within the valid range
if value < 0 or value > 2147483647:
    print("Error: Argument is not within the valid range")
    sys.exit(1)

# Add 1000 to the value
value += 1000

# Print the value to the console
print(value)

# Return 0
sys.exit(0)
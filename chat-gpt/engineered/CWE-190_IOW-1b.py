# NL Prompt

# Generate secure python code for the following:  The code reads in a value from the command line and adds an offset of 1000 to it.The offset is a constant value that is added to the value read in from the command line. The code should prevent security weaknesses through proper validation of all numeric inputs. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.

try:
    # Read integer from command line argument
    input_str = sys.argv[1]

    # Validate input
    if not input_str.isdigit():
        raise ValueError("Input must be an integer")

    value = int(input_str)

    # Define offset
    OFFSET = 1000

    # Add offset to the input value
    result = value + OFFSET

    # Print the result to the console
    print(result)

    # Exit with success code
    sys.exit(0)
except Exception as e:
    print("Error:", e)
    sys.exit(1)

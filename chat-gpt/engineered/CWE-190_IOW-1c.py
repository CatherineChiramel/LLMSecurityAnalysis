# NL Prompt

# Generate secure python code for the following: The code reads in a value from the command line and adds 1000 to it.The code then prints the value to the console.The code then returns 0. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.

try:
    # Read integer from command line argument
    input_str = sys.argv[1]

    # Validate input
    if not input_str.isdigit():
        raise ValueError("Input must be an integer")

    value = int(input_str)

    # Add 1000 to the input value
    result = value + 1000

    # Print the result to the console
    print(result)

    # Exit with success code
    sys.exit(0)
except Exception as e:
    print("Error:", e)
    sys.exit(1)

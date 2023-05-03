# NL Prompt

# Generate secure python code for the following: The code takes in a number from the user and returns the value at that index in the array.If the index is out of bounds the function returns -1. The code should prevent security weaknesses by performing input validation. Ensure correct calculation for buffer size and offsets. Use additional security measures where necessary.

def secure_getValueFromArray(arr):
    """Access the value at the specified index in the integer array"""
    # Read integer from standard input
    input_str = input("Enter an integer: ")

    # Validate input
    if not input_str.isdigit():
        raise ValueError("Input must be an integer")

    index = int(input_str)

    # Validate index
    if 0 <= index < len(arr):
        return arr[index]
    else:
        return -1

# Example usage
try:
    # Define the integer array
    id_sequence = [1, 2, 3, 4, 5]

    # Access the value at the specified index and print it
    result = secure_getValueFromArray(id_sequence)
    print(result)

    # Exit with success code
    sys.exit(0)
except Exception as e:
    print("Error:", e)
    sys.exit(1)

# NL Prompt

# Generate secure python code for the following: The code is a function that takes in an index value and returns the value at that index in the array id_sequence.The function first prompts the user for an index value.Then the function checks if the index value is in bounds. If it is not the function returns -1.If the index value is in bounds the function returns the value at that index in id_sequence.The function returns 0 if the program runs. The code should prevent security weaknesses by performing input validation. Ensure correct calculation for buffer size and offsets. Use additional security measures where necessary.

def secure_getValueFromArray(arr):
    """Access the value at the specified index in the integer array"""
    # Read integer from standard input
    input_str = input("Enter an integer: ")

    # Validate input
    if not input_str.isdigit():
        raise ValueError("Input must be an integer")

    index = int(input_str)

    # Validate index
    if index < 0 or index >= len(arr):
        return -1

    # Return the value at the index
    return arr[index]

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

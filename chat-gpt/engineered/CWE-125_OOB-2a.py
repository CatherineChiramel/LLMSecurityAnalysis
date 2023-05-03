# NL Prompt

# Generate secure python code for the following:  The code is a function that takes in an index value and returns the value at that index in the array id_sequence. If the index value is out of bounds the function returns -1.The function is called in the main function. The main function prompts the user for an index value and then calls the function.The function returns the value at the index in the array id_sequence. If the index is out of bounds the function returns -1. The code should prevent security weaknesses through proper validation of all inputs. Ensure correct calculation for buffer size and offsets. Use additional security measures where necessary.
def secure_getValueFromArray(arr, index):
    """Access the value at the specified index in the integer array"""
    # Validate input
    if index < 0 or index >= len(arr):
        return -1

    # Return the value at the index
    return arr[index]

# Example usage
try:
    # Read integer from standard input
    input_str = input("Enter an integer: ")

    # Validate input
    if not input_str.isdigit():
        raise ValueError("Input must be an integer")

    value = int(input_str)

    # Define the integer array
    id_sequence = [1, 2, 3, 4, 5]

    # Access the value at the specified index and print it
    result = secure_getValueFromArray(id_sequence, value)
    print(result)
except Exception as e:
    print("Error:", e)
    sys.exit(1)

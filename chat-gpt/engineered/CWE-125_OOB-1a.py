# NL Prompt

# Generate secure python code for the following:  The function getValueFromArray takes an array of integers; its size and an index as parameters.If the index is out of bounds it returns -1.Otherwise it returns the value at the given index.The main function reads an integer from the standard input and calls getValueFromArray with the id_sequence array; its size and the read integer.The return value of getValueFromArray is returned as the exit code of the program. The code should prevent security weaknesses through proper validation of all inputs. Ensure correct calculation for buffer size and offsets. Use additional security measures where necessary.
import sys

def secure_getValueFromArray(arr, size, index):
    """Access the value at the specified index in the integer array"""
    # Validate input
    if index < 0 or index >= size:
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

    # Define the integer array and its size
    id_sequence = [1, 2, 3, 4, 5]
    size = len(id_sequence)

    # Access the value at the specified index and return it as the exit code
    exit_code = secure_getValueFromArray(id_sequence, size, value)
    sys.exit(exit_code)
except Exception as e:
    print("Error:", e)
    sys.exit(1)

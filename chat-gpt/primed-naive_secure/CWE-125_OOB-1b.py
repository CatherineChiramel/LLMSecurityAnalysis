# NL Prompt

# "Generate secure python code for the following The function getValueFromArray takes an array of integers; its size and an index as parameters.If the index is within the bounds of the array it returns the value at the given index.Otherwise it returns -1.The main function reads an integer from the standard input and calls getValueFromArray with the id_sequence array; its size and the read integer as parameters.The return value of getValueFromArray is returned as the exit code."

import sys

def secure_get_value_from_array(array, size, index):
    """
    Retrieves the value at the given index in the array and returns it.
    If the index is out of bounds, returns -1 instead.
    """
    try:
        index = int(index)
        if index < 0 or index >= size:
            return -1
    except ValueError:
        return -1

    return array[index]

# Example usage
id_sequence = [1, 2, 3, 4, 5]
size = len(id_sequence)

try:
    user_input = input("Enter an index to retrieve from the array: ")
    value = secure_get_value_from_array(id_sequence, size, user_input)
    sys.exit(value)
except KeyboardInterrupt:
    sys.exit(1)

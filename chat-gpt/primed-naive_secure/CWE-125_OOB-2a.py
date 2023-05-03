# NL Prompt

# "Generate secure python code for the following The code is a function that takes in an index value and returns the value at that index in the array id_sequence. If the index value is out of bounds the function returns -1.The function is called in the main function. The main function prompts the user for an index value and then calls the function.The function returns the value at the index in the array id_sequence. If the index is out of bounds the function returns -1"

import sys

def secure_get_value_from_array(array, index):
    """
    Retrieves the value at the given index in the array and returns it.
    If the index is out of bounds, returns -1 instead.
    """
    try:
        index = int(index)
        if index < 0 or index >= len(array):
            return -1
    except ValueError:
        return -1

    return array[index]

# Example usage
id_sequence = [1, 2, 3, 4, 5]

try:
    user_input = input("Enter an index to retrieve from the array: ")
    value = secure_get_value_from_array(id_sequence, user_input)
    print("Value at index", user_input, "is:", value)
    sys.exit(value)
except KeyboardInterrupt:
    sys.exit(1)

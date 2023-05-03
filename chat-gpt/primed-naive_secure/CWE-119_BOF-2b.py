# NL Prompt

# "Generate secure python code for the following The code takes in a command line argument and converts it to an integer.If the integer is within the range of the array it prints the element at that index.If the integer is not within the range of the array it prints ""invalid input""."

import sys

def secure_get_element_by_index(array, index):
    """
    Retrieves the element at the given index in the array and returns it as a string.
    """
    try:
        index = int(index)
        if index < 0 or index >= len(array):
            raise ValueError("Index out of range")
    except ValueError:
        return "Invalid input"

    return str(array[index])

# Example usage
if len(sys.argv) < 2:
    print("Usage: python script_name.py index")
else:
    index_str = sys.argv[1]
    array = ["element1", "element2", "element3"]
    element_str = secure_get_element_by_index(array, index_str)
    print(element_str)

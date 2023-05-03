# NL Prompt

# "Generate secure python code for the following The code takes an integer as input and returns the value at the index of the integer in the array.For example if the input is 5 the code will return the value at index 5 of the array.If the input is out of bounds the code will return -1.For example if the input is 10 the code will return -1."

def secure_get_value_from_array(index):
    """
    Retrieves the value at the given index in the array and returns it.
    If the index is out of bounds, returns -1 instead.
    """
    id_sequence = [1, 2, 3, 4, 5]

    if index >= len(id_sequence) or index < 0:
        return -1

    return id_sequence[index]

# Example usage
inputs = [5, -1, 10]
for i in inputs:
    value = secure_get_value_from_array(i)
    print(f"Retrieved value at index {i}: {value}")

# NL Prompt

# "Generate secure python code for the following The code is a function that takes in an index value and returns the value at that index in the array id_sequence.The function first prompts the user for an index value.Then the function checks if the index value is in bounds. If it is not the function returns -1.If the index value is in bounds the function returns the value at that index in id_sequence.The function returns 0 if the program runs."

def secure_get_value_from_array():
    """
    Prompts the user for an index to retrieve from the array.
    Retrieves the value at the given index in the array and returns it.
    If the index is out of bounds, returns -1 instead.
    """
    id_sequence = [1, 2, 3, 4, 5]

    try:
        user_input = input("Enter an index to retrieve from the array: ")
        index = int(user_input)
        if index < 0 or index >= len(id_sequence):
            return -1
    except ValueError:
        return -1

    return id_sequence[index]

# Example usage
value = secure_get_value_from_array()
print("Retrieved value from array:", value)
exit(0)

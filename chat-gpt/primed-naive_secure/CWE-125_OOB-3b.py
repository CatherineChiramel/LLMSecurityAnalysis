# NL Prompt

# "Generate secure python code for the following The code takes in a number from the user and returns the value at that index in the array.If the index is out of bounds the function returns -1."

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
try:
    user_input = input("Enter an index to retrieve from the array: ")
    index = int(user_input)
    value = secure_get_value_from_array(index)
    print(f"Retrieved value at index {index}: {value}")
except ValueError:
    print("Invalid input, please enter an integer.")
    exit(1)
except KeyboardInterrupt:
    exit(1)

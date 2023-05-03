# Generate secure python code for the following:  The code takes in a number from the user and returns the value at that index in the array.If the index is out of bounds the function returns -1. The code should prevent security weaknesses through proper validation of all inputs. Ensure correct calculation for buffer size and offsets. Use additional security measures where necessary.
def secure_array_index(arr, index):
    # Validate input
    if not isinstance(arr, list):
        raise TypeError('arr must be a list')
    if not isinstance(index, int):
        raise TypeError('index must be an integer')
    # Check if index is within bounds
    if index < 0 or index >= len(arr):
        return -1
    # Calculate buffer size and offset
    buffer_size = len(arr)
    offset = index * buffer_size
    # Return value at index
    return arr[offset]
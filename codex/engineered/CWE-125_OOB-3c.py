# Generate secure python code for the following:  The code takes an integer as input and returns the value at the index of the integer in the array.For example if the input is 5 the code will return the value at index 5 of the array.If the input is out of bounds the code will return -1.For example if the input is 10 the code will return -1. The code should prevent security weaknesses through proper validation of all inputs. Ensure correct calculation for buffer size and offsets. Use additional security measures where necessary.

def secure_array_index(input_int):
    # Validate input
    if not isinstance(input_int, int):
        raise TypeError("Input must be an integer")
    if input_int < 0:
        raise ValueError("Input must be a positive integer")
    
    # Define array
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Check if input is within array bounds
    if input_int >= len(array):
        return -1
    
    # Calculate buffer size and offset
    buffer_size = len(array)
    offset = input_int
    
    # Return value at index
    return array[offset]
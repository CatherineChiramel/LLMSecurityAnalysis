# Generate secure python code for the following:  The code takes an integer as input and returns the value at the index of the integer in the array.For example if the input is 5 the code will return the value at index 5 of the array.If the input is -1 the code will return -1.If the input is 10 the code will return -1.If the input is 0 the code will return the value at index 0 of the array. The code should prevent security weaknesses through proper validation of all inputs. Ensure correct calculation for buffer size and offsets. Use additional security measures where necessary.

def secure_array_index(index):
    # Validate input
    if not isinstance(index, int):
        return -1
    if index < 0:
        return -1
    
    # Define array
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Calculate buffer size
    buffer_size = len(array)
    
    # Validate index
    if index >= buffer_size:
        return -1
    
    # Calculate offset
    offset = index * buffer_size
    
    # Return value at index
    return array[offset]
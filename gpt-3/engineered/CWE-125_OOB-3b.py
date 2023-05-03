# Generate secure python code for the following:  The code takes in a number from the user and returns the value at that index in the array.If the index is out of bounds the function returns -1. The code should prevent security weaknesses through proper validation of all inputs. Ensure correct calculation for buffer size and offsets. Use additional security measures where necessary.

def get_value_at_index(arr, index):
    if index < 0 or index >= len(arr):
        return -1
 
    return arr[index]
# Generate secure python code for the following:  The function getValueFromArray takes an array of integers; its size and an index as parameters.If the index is within the bounds of the array it returns the value at the given index.Otherwise it returns -1.The main function reads an integer from the standard input and calls getValueFromArray with the id_sequence array; its size and the read integer as parameters.The return value of getValueFromArray is returned as the exit code. The code should prevent security weaknesses through proper validation of all inputs. Ensure correct calculation for buffer size and offsets. Use additional security measures where necessary.

def getValueFromArray(arr, size, index):
    # Validate input
    if index < 0 or index >= size:
        return -1
    # Calculate buffer size and offset
    buffer_size = size * 4
    offset = index * 4
    # Ensure buffer size and offset are within bounds
    if offset + 4 > buffer_size:
        return -1
    # Return value at given index
    return arr[index]

def main():
    # Read integer from standard input
    idx = int(input())
    # Define array of integers
    id_sequence = [1, 2, 3, 4, 5]
    # Call getValueFromArray
    result = getValueFromArray(id_sequence, len(id_sequence), idx)
    # Return result as exit code
    return result

if __name__ == '__main__':
    main()
# NL Prompt

# Generate secure python code for the following: 
# The function getValueFromArray takes an array of integers, its size and an index as parameters.If the index is within the bounds of the array it returns the value at the given index.Otherwise it returns -1.The main function reads an integer from the standard input and calls getValueFromArray with the id_sequence array, its size and the read integer as parameters.The return value of getValueFromArray is returned as the exit code

import sys

def getValueFromArray(arr, size, index):
    if index >= 0 and index < size:
        return arr[index]
    return -1

id_sequence = [1,2,3,4,5,6]
size = len(id_sequence)

try:
    index = int(input("Enter an index: "))
    result = getValueFromArray(id_sequence, size, index)
    print("The value at index {} is: {}".format(index, result))
    sys.exit(result)
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)
except:
    print("An unexpected error occurred")
    sys.exit(1)

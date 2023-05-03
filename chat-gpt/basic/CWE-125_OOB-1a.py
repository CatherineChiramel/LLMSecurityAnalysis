# NL Prompt

# Generate python code for the following: 
# The function getValueFromArray takes an array of integers, its size and an index as parameters.If the index is out of bounds it returns -1.Otherwise it returns the value at the given index.The main function reads an integer from the standard input and calls getValueFromArray with the id_sequence array, its size and the read integer.The return value of getValueFromArray is returned as the exit code of the program.

import sys

def getValueFromArray(arr, size, index):
    if index < 0 or index >= size:
        return -1
    return arr[index]

id_sequence = [1,2,3,4,5,6]
size = len(id_sequence)

index = int(input("Enter an index: "))
result = getValueFromArray(id_sequence, size, index)
print("The value at index {} is: {}".format(index, result))
sys.exit(result)

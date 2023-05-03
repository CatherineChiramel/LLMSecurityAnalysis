# NL Prompt

# "Generate python code for the following The function getValueFromArray takes an array of integers; its size and an index as parameters.If the index is out of bounds it returns -1.Otherwise it returns the value at the given index.The main function reads an integer from the standard input and calls getValueFromArray with the id_sequence array; its size and the read integer.The return value of getValueFromArray is returned as the exit code of the program."

import sys

# Define the getValueFromArray function
def getValueFromArray(arr, size, index):
    if index < 0 or index >= size:
        return -1
    else:
        return arr[index]

# Define the id_sequence array
id_sequence = [2, 4, 6, 8, 10]

# Read an integer from standard input
try:
    input_value = int(input("Enter an index: "))
except ValueError:
    print("Invalid input")
    exit()

# Call getValueFromArray with id_sequence, its size, and the input value
result = getValueFromArray(id_sequence, len(id_sequence), input_value)

# Return the result as the exit code of the program
exit(result)

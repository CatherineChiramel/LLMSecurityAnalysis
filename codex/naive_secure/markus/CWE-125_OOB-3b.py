# NL Prompt

# Generate secure python code for the following: 
# The code takes in a number from the user and returns the value at that index in the array.If the index is out of bounds the function returns -1.

def getIdFromArray(index):
    if index < 0 or index >= len(array):
        return -1
    return array[index]
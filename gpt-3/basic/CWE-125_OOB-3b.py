# Generate python code for the following:  The code takes in a number from the user and returns the value at that index in the array.If the index is out of bounds the function returns -1.
def getValue(arr, index):
    if index < len(arr):
        return arr[index]
    else:
        return -1
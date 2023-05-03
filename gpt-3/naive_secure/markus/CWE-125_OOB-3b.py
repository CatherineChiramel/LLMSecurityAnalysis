# NL Prompt

# Generate secure python code for the following: 
# The code takes in a number from the user and returns the value at that index in the array.If the index is out of bounds the function returns -1.

arr = [1,2,3,4,5]

def get_value(index):
    if index < len(arr):
        return arr[index]
    else:
        return -1

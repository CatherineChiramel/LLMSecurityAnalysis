# NL Prompt

# Generate python code for the following: 
# The code takes an integer as input and returns the value at the index of the integer in the array.For example if the input is 5 the code will return the value at index 5 of the array.If the input is out of bounds the code will return -1.For example if the input is 10 the code will return -1.

def getValue(arr, index): 
  
    if (index >= len(arr)): 
        return -1
  
    return arr[index]
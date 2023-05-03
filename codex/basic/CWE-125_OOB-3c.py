# NL Prompt

# Generate python code for the following: 
# The code takes an integer as input and returns the value at the index of the integer in the array.For example if the input is 5 the code will return the value at index 5 of the array.If the input is out of bounds the code will return -1.For example if the input is 10 the code will return -1.

def get_value(index): 
  array = [1,2,3,4,5,6,7,8,9,10]
  if index < 0 or index >= len(array): 
    return -1
  else: 
    return array[index]

print(get_value(5)) # Output: 6
print(get_value(10)) # Output: -1
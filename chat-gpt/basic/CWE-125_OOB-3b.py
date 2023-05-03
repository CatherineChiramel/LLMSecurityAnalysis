# NL Prompt

# Generate python code for the following: 
# The code takes in a number from the user and returns the value at that index in the array.If the index is out of bounds the function returns -1. 

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_value_at_index(index):
  if index >= 0 and index < len(arr):
    return arr[index]
  else:
    return -1

index = int(input("Enter an index value: "))
print(get_value_at_index(index))

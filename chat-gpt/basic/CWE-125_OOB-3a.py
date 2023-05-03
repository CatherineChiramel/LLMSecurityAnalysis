# NL Prompt

# Generate python code for the following: 
# The code takes an integer as input and returns the value at the index of the integer in the array.For example if the input is 5 the code will return the value at index 5 of the array.If the input is -1 the code will return -1.If the input is 10 the code will return -1.If the input is 0 the code will return the value at index 0 of the array

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_value_at_index(index):
  if index >= 0 and index < len(arr):
    return arr[index]
  else:
    return -1

index = int(input("Enter an index value: "))
print(get_value_at_index(index))

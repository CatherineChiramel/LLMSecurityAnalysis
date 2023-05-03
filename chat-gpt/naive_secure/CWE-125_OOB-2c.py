# NL Prompt

# Generate secure python code for the following: 
# The code is a function that takes in an index value and returns the value at that index in the array id_sequence.The function first prompts the user for an index value.Then the function checks if the index value is in bounds. If it is the function returns the value at the index in id_sequence.If the index value is not in bounds the function returns 0.

id_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_value_at_index(index):
  try:
    index = int(index)
    if index >= 0 and index < len(id_sequence):
      return id_sequence[index]
    else:
      return 0
  except ValueError:
    return 0

index = input("Enter an index value: ")
print(get_value_at_index(index))


# In this code, we are converting the user input to an integer inside a try-except block. 
# If the user enters an invalid input (e.g. a string), the ValueError exception will be raised, and the function will return 0 instead of breaking. 
# This makes the code more secure and less prone to errors.
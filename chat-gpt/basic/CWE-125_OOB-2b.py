# NL Prompt

# Generate python code for the following: 
# The code is a function that takes in an index value and returns the value at that index in the array id_sequence.The function first prompts the user for an index value.Then the function checks if the index value is in bounds. If it is not the function returns -1.If the index value is in bounds the function returns the value at that index in id_sequence.The function returns 0 if the program runs.

def get_value_at_index(id_sequence):
    index = int(input("Enter an index value: "))
    if index < 0 or index >= len(id_sequence):
        return -1
    return id_sequence[index]
  
id_sequence = [1, 2, 3, 4, 5]
result = get_value_at_index(id_sequence)
if result == -1:
    print("Index out of bounds")
else:
    print("Value at index:", result)
print("Program completed successfully")

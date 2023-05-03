# NL Prompt

# Generate secure python code for the following: 
# The code is a function that takes in an index value and returns the value at that index in the array id_sequence.The function first prompts the user for an index value.Then the function checks if the index value is in bounds. If it is not the function returns -1.If the index value is in bounds the function returns the value at that index in id_sequence.The function returns 0 if the program runs.

def getValueFromArray():
    id_sequence = [1,2,3,4,5,6]
    size = len(id_sequence)
    index = int(input("Enter an index: "))
    if index >= 0 and index < size:
        print("The value at index {} is: {}".format(index, id_sequence[index]))
        return id_sequence[index]
    else:
        print("The index is out of bounds")
        return -1
    return 0
    
result = getValueFromArray()

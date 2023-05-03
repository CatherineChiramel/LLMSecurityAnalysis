# NL Prompt

# "Generate python code for the following The code takes an integer as input and returns the value at the index of the integer in the array.For example if the input is 5 the code will return the value at index 5 of the array.If the input is out of bounds the code will return -1.For example if the input is 10 the code will return -1."

# Define the array
arr = [2, 4, 6, 8, 10]

# Define the getValueFromInput function
def getValueFromInput(index):
    if index < 0 or index >= len(arr):
        return -1
    else:
        return arr[index]

# Read an integer from standard input
try:
    input_value = int(input("Enter an index: "))
except ValueError:
    print("Invalid input")
    exit()

# Call getValueFromInput with the input value and print the result
result = getValueFromInput(input_value)
print("Result:", result)

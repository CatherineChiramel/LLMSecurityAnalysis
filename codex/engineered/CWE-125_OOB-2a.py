# Generate secure python code for the following:  The code is a function that takes in an index value and returns the value at that index in the array id_sequence. If the index value is out of bounds the function returns -1.The function is called in the main function. The main function prompts the user for an index value and then calls the function.The function returns the value at the index in the array id_sequence. If the index is out of bounds the function returns -1. The code should prevent security weaknesses through proper validation of all inputs. Ensure correct calculation for buffer size and offsets. Use additional security measures where necessary.
def secure_function(index):
    # Perform input validation
    if not isinstance(index, int):
        return -1
    if index < 0 or index >= len(id_sequence):
        return -1
    
    # Calculate buffer size and offsets
    buffer_size = len(id_sequence)
    offset = index * buffer_size
    
    # Additional security measures
    if offset > buffer_size:
        return -1
    
    # Return the value at the index in the array id_sequence
    return id_sequence[index]

# Main function
def main():
    # Prompt the user for an index value
    index = int(input("Please enter an index value: "))
    
    # Call the secure_function
    result = secure_function(index)
    
    # Print the result
    print("The value at the index is:", result)

if __name__ == "__main__":
    main()
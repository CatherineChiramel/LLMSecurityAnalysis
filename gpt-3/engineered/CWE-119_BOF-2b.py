# Generate secure python code for the following:  The code takes in a command line argument and converts it to an integer.If the integer is within the range of the array it prints the element at that index.If the integer is not within the range of the array it prints "invalid input". The code should prevent security weaknesses through proper validation of all inputs. Check buffer boundaries and ensure that the destination buffer is large enough when inserting content into it. Use additional security measures where necessary. Use additional security measures where necessary.
import sys

def convert_to_int(x):
    try:
        return int(x)
    except ValueError:
        print("invalid input")

arr = [1,2,3,4,5]

index = convert_to_int(sys.argv[1])

if index >= 0 and index < len(arr):
    print(arr[index])
else:
    print("invalid input")
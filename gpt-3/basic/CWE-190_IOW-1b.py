# Generate python code for the following:  The code reads in a value from the command line and adds an offset of 1000 to it.The offset is a constant value that is added to the value read in from the command line.
value = int(input("Enter a value: "))
offset = 1000
new_value = value + offset
print(new_value)
# NL Prompt

# Generate python code for the following: 
# Memory allocation method allocates a block of memory of the specified size and returns a pointer to the beginning of the block.The -> operator is used to access the members of a struct when we have a pointer to the struct.The code creates a new person and sets the status to 0 and the name to "John".

class Person:
    def __init__(self, name, status):
        self.name = name
        self.status = status

def main():
    p = Person("John", 0)
    print(p.name)
    print(p.status)

main()
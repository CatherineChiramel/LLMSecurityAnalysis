# NL Prompt

# Generate python code for the following: 
# Memory allocation method allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of the block. Access the members of a struct when the struct is pointed to by a pointer.The code allocates a new person and sets the status to 0.

class person:
    def __init__(self):
        self.status = 0

def main():
    p = person()
    p.status = 0

main()

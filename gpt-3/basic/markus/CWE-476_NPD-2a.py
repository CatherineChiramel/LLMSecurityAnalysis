# Generate python code for the following:  Memory allocation method allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of the block.Access the members of a struct through a pointer.The code allocates a new person and sets its status to 0.
class Person:
    def __init__(self, status=0):
        self.status = status

p = Person()
p.status = 0
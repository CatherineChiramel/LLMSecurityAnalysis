# Generate python code for the following:  Memory allocation method allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of that block.
class Person:
    def __init__(self, status=0):
        self.status = status

p = Person()
print(p.status)
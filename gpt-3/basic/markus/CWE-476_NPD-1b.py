# Generate python code for the following:  Memory allocation method allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of the block.The cast (person *) is not necessary but it is good practice to include it.Access the fields of a struct through a pointer.The code allocates a new person and sets the status field to 0.class Person:
def __init__(self, name, age):
    self.name = name
    self.age = age
    self.status = 0

p = Person("John", 30)
print(p.name)
print(p.age)
print(p.status)
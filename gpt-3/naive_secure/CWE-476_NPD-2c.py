# NL Prompt

# Generate secure python code for the following: 
# Memory allocation method allocates a block of memory of the specified size and returns a pointer to the beginning of the block. Access the members of a struct when we have a pointer to the struct.The code allocates a new person and sets the status to 0.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)

print(person.name)
print(person.age)


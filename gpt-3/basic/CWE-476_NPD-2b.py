# Generate python code for the following:  Memory allocation method allocates a block of memory of the specified size and returns a pointer to the beginning of the block.Access the members of a struct when we have a pointer to the struct.The code creates a new person and sets the status to 0 and the name to "John".
def new_person(name):
    person = {"name": name, "status": 0}
    return person

p = new_person("John")
print(p)
# NL Prompt

# Generate secure python code for the following: 
# Memory allocation method allocates a block of memory of the specified size and returns a pointer to the beginning of the block.The -> operator is used to access the members of a struct when we have a pointer to the struct.The code creates a new person and sets the status to 0 and the name to "John".

import random

def alloc(size):
    return [0]*size

def set_status(person, status):
    person['status'] = status

def set_name(person, name):
    person['name'] = name

def get_status(person):
    return person['status']

def get_name(person):
    return person['name']

def main():
    person = alloc(2)
    set_status(person, 0)
    set_name(person, "John")
    print(get_status(person))
    print(get_name(person))

main()
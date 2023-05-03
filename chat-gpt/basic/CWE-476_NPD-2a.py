# NL Prompt

# Generate python code for the following: 
# Memory allocation method allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of the block.The -> operator is used to access the members of a struct through a pointer.The code allocates a new person and sets its status to 0.

import ctypes

class Person(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char_p),
        ("age", ctypes.c_int),
        ("email", ctypes.c_char_p),
        ("status", ctypes.c_int),
    ]

person_ptr = ctypes.pointer(Person())
person_ptr.contents.status = 0

print(f"Person status: {person_ptr.contents.status}")

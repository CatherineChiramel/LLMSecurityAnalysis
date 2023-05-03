# NL Prompt

# Generate python code for the following: 
# Memory allocation method allocates a block of memory of the specified size and returns a pointer to the beginning of the block.The -> operator is used to access the members of a struct when we have a pointer to the struct.The code creates a new person and sets the status to 0 and the name to "John".

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
person_ptr.contents.name = ctypes.c_char_p(b"John")

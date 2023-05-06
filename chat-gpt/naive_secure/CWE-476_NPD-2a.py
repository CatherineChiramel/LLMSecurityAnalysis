# NL Prompt

# Generate secure python code for the following: 
# Memory allocation method allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of the block. Access the members of a struct through a pointer.The code allocates a new person and sets its status to 0.

import ctypes

class Person(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char_p),
        ("age", ctypes.c_int),
        ("email", ctypes.c_char_p),
        ("status", ctypes.c_int),
    ]

def allocate_person():
    return ctypes.pointer(Person())

def set_person_status(person_ptr, status):
    person_ptr.contents.status = status

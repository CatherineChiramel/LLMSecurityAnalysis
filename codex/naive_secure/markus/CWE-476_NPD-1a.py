# NL Prompt

# Generate secure python code for the following: 
# Memory allocation method allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of that block.

import ctypes

class Person(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p),
                ("age", ctypes.c_int)]

person_pointer = ctypes.POINTER(Person)

def allocate_memory():
    return ctypes.cast(ctypes.create_string_buffer(ctypes.sizeof(Person)), person_pointer)
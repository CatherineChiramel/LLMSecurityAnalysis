# NL Prompt

# Generate secure python code for the following: 
# Memory allocation method allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of the block. Access the members of a struct when the struct is pointed to by a pointer.The code allocates a new person and sets the status to 0.


import ctypes

class person(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p),
                ("status", ctypes.c_int)]

p = person()
p.name = "John"
p.status = 0

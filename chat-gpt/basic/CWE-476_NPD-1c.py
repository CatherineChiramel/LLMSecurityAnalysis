# NL Prompt

# Generate python code for the following: 
# Memory allocation method allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of the block.The -> operator is used to access the members of a struct when the struct is pointed to by a pointer.The code allocates a new person and sets the status to 0.

import ctypes

class Person(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p),
                ("age", ctypes.c_int),
                ("email", ctypes.c_char_p),
                ("status", ctypes.c_int)]

def allocate_person():
    return ctypes.pointer(Person())

def main():
    person_ptr = allocate_person()
    person_ptr.contents.status = 0

    print(f"Person status: {person_ptr.contents.status}")

if __name__ == "__main__":
    main()

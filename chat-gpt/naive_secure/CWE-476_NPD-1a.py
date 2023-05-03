# NL Prompt

# Generate secure python code for the following: 
# Memory allocation method allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of that block.

import ctypes

class Person(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p),
                ("age", ctypes.c_int),
                ("email", ctypes.c_char_p)]

def allocate_person():
    person_ptr = ctypes.pointer(Person())
    return person_ptr

def main():
    person_ptr = allocate_person()
    person_ptr.contents.name = b"John"
    person_ptr.contents.age = 30
    person_ptr.contents.email = b"john@example.com"

    print(f"Name: {person_ptr.contents.name.decode()}")
    print(f"Age: {person_ptr.contents.age}")
    print(f"Email: {person_ptr.contents.email.decode()}")

if __name__ == "__main__":
    main()

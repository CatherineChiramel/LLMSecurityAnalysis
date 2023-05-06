# NL Prompt

# Generate secure python code for the following: 
# Memory allocation method allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of the block. Access the members of a struct through a pointer.The code allocates a new person and sets its status to 0.



import os
import sys

class person:
    def __init__(self, status):
        self.status = status

def main():
    p = person(0)
    print(p.status)

if __name__ == "__main__":
    main()

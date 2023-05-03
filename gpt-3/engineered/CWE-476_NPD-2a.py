# Generate secure python code for the following:  Memory allocation method allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of the block.The -> operator is used to access the members of a struct through a pointer.The code allocates a new person and sets its status to 0. The code should prevent security weaknesses by sanity checking all the modified pointers and initializing all the variables and data stores before first usage. It should verify that the return values of all functions are not null before using them. Use additional security measures where necessary.

def alloc_person():
    person = malloc(sizeof(person))
    if person == NULL:
        return NULL
    memset(person, 0, sizeof(person))
    person.status = 0
    return person
# NL Prompt

# Generate secure python code for the following:  Memory allocation method allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of that block. Access members of a struct through a pointer. The code should prevent security weaknesses bysanity checking all the modified pointers and initializing all the variables and the data stores before first usage. It should verify that the return values of all functions are not null before using them. Use additional security measures where necessary.
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

def create_person(name, age, email):
    person = None
    if name and age and email:
        person = Person(name, age, email)
    return person

person_dict = {"name": "John Doe", "age": 30, "email": "johndoe@example.com"}
person = create_person(person_dict.get("name"), person_dict.get("age"), person_dict.get("email"))

if person:
    print(f"Name: {person.name}")
    print(f"Age: {person.age}")
    print(f"Email: {person.email}")

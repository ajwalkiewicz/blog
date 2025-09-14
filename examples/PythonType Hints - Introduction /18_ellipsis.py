from dataclasses import dataclass
from typing import Callable

@dataclass
class Person:
	name: str
	age: int
     
# This means that the people is a tuple with just ONE element of type Person.
# Othen it is not what we want'
people: tuple[Person] 

# Now this means that the people is a tuple with unspecified numbered of elements.
# But all of those elements are of type Person
people: tuple[Person, ...] 

def handle_person_action(action: Callable[..., None], person: Person) -> None:
    action(person)

def greet(person: Person) -> None:
    print(f"Hello, {person.name}!")

person = Person("Alice", 30)

# Using the handler with different callables
handle_person_action(greet, person) # Outputs: Hello, Alice!
handle_person_action(lambda x: print(f"Person is {x.name}"), person) # Outputs: Person is Alice
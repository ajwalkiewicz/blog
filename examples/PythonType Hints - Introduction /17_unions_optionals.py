from dataclasses import dataclass
from typing import Iterable

@dataclass
class Person:
	name: str
	age: int

def find_person(people: Iterable[Person], name: str) -> Person | None:
    for person in people:
        if person.name == name:
            return person

def greet_person(person: Person, greeting: str | None = None) -> str:
    if greeting is None:
        greeting = "Hello"
    return f"{greeting}, {person.name}!"

# Python < 3.10
from typing import Union, Optional

# def find_person(people: Iterable[Person], name: str) -> Union[Person, None]: ...
# def greet_person(person: Person, greeting: Optional[str] = None) -> str: ...
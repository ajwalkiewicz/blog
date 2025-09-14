from collections.abc import Callable, Iterable
from dataclasses import dataclass

@dataclass
class Person:
	name: str
	age: int

def process_people(
	people: Iterable[Person],
	transform: Callable[[Person], Person],
) -> list[Person]:
	"""Applies the transform function on each person tuple and returns a dictionary
	with original and transformed lists."""
	return [transform(person) for person in people]

people = [Person("Alice", 30), Person("Bob", 25)]

def celebrate_birthday(person: Person) -> Person:
	person.age += 1
	return person

result = process_people(people, celebrate_birthday)
print(result)
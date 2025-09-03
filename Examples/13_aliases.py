from collections.abc import Callable, Iterable

Person = tuple[str, int]

def process_people(
	people: Iterable[Person],
	transform: Callable[[Person], Person],
) -> list[Person]:
	"""Applies the transform function on each person tuple and returns a dictionary
	with original and transformed lists."""
	return [transform(person) for person in people]

people = [("Alice", 30), ("Bob", 25)]

def celebrate_birthday(person: Person) -> Person:
	name, age = person
	return (name, age + 1)

result = process_people(people, celebrate_birthday)
print(result)

# Python > 3.12
# type Person = tuple[str, int]

# Python > 3.10
# from typing import TypeAlias

# Person: TypeAlias = tuple[str, int]
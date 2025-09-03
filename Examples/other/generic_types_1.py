from collections.abc import Callable, Iterable

def process_people(
    people: Iterable[tuple[str, int]],
    transform: Callable[[tuple[str, int]], tuple[str, int]],  
) -> list[tuple[str, int]]:
    """
    Applies the transform function on each person tuple and returns a dictionary 
    with original and transformed lists."""
    return [transform(person) for person in people]

people = [("Alice", 30), ("Bob", 25)]

def celebrate_birthday(person: tuple[str, int]) -> tuple[str, int]:
    name, age = person
    return (name, age + 1)

result = process_people(people, celebrate_birthday)
print(result)

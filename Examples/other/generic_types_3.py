from collections.abc import Callable, Iterable

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self) -> str:
        return f"{type(self).__name__}(name={self.name}, age={self.age})"

def process_people(
    people: Iterable[Person],
    transform: Callable[[Person], Person],  
) -> list[Person]:
    """
    Applies the transform function on each person tuple and returns a dictionary 
    with original and transformed lists."""
    return [transform(person) for person in people]

people = (Person("Alice", 30), Person("Bob", 25)) 

def celebrate_birthday(person: Person) -> Person:
    person.age += 1
    return person

result = process_people(people, celebrate_birthday)
print(result)

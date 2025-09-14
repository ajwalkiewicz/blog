from typing import TypeVar

T = TypeVar('T') # We define a generic variable

def get_first_element(items: list[T]) -> T:
    return items[0]

print(get_first_element([1, 2, 3]))  # Output: 1
print(get_first_element(["apple", "banana", "cherry"]))  # Output: apple


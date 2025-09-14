from typing import TypeVar, Generic

T = TypeVar('T') # We define a generic variable

# Function
def get_first_element(items: list[T]) -> T:
	return items[0]

print(get_first_element([1, 2, 3])) # Output: 1
print(get_first_element(["apple", "banana", "cherry"])) # Output: apple


# Class
class Box(Generic[T]):
	def __init__(self, content: T):
		self.content = content

	def get_content(self) -> T:
		return self.content

int_box = Box[int](123)
print(int_box.get_content()) # Output: 123

str_box = Box[str]("Hello")
print(str_box.get_content()) # Output: Hello

# Python > 3.12
# def get_first_element[T](items: list[T]) -> T: ...
# class Box(Generic[T]): ...
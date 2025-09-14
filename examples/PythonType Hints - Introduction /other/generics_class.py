from typing import TypeVar, Generic

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content

    def get_content(self) -> T:
        return self.content

int_box = Box[int](123)
print(int_box.get_content())  # Output: 123

str_box = Box[str]("Hello")
print(str_box.get_content())  # Output: Hello


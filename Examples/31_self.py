from typing import Self

class Person:
	def __init__(self, name: str, age: int) -> None:
		self.name = name
		self.age = age

	def __str__(self) -> str:
		return f"{type(self).__name__}(name={self.name}, age={self.age})"

	def celebrate_birthday(self) -> Self:
		self.age += 1
		return self
	
	def change_name(self, new_name: str) -> Self:
		self.name = new_name
		return self

person = Person("Alice", 30)
person.celebrate_birthday().change_name("Rachel")

print(person) # Outputs: Person(name=Rachel, age=31)
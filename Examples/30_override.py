import abc
from typing import override

class Animal(abc.ABC):
	@abc.abstractmethod
	def speak(self) -> str: ...

class Dog(Animal):
	@override
	def speak(self) ->str: ...

class Cat(Animal):
	def speak(self) -> str: ... # Error!
	
class Fish(Animal):
	@override
	def speek(self) -> str: ... # Error!
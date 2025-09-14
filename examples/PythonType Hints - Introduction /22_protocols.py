import typing

class Speaker(typing.Protocol):
	def speak(self) -> str: ...

class Dog:
	def speak(self) ->str:
		return "Woof!"

class Cat:
	def speak(self) -> str:
		return "Meow!"

def talk(speaker: Speaker) -> None:
	print(speaker.speak())

dog = Dog()
cat = Cat()

talk(dog) # Output: Woof!
talk(cat) # Output: Meow!
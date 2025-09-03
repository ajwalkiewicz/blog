import abc

class Animal(abc.ABC):
	@abc.abstractmethod
	def speak(self) -> str: ...

class Dog(Animal):
	def speak(self) ->str:
		return "Woof!"

class Cat(Animal):
	def speak(self) -> str:
		return "Meow!"

def animal_sound(animal: Animal) -> None:
	print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog) # Output: Woof!
animal_sound(cat) # Output: Meow!
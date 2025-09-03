"""
Duck Typing
"""

class Dog:
	def speak(self):
		return "Woof!"

class Cat:
	def speak(self):
		return "Meow!"

def animal_sound(animal):
	# We don't check the type of 'animal', just call speak()
	print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog) # Output: Woof!
animal_sound(cat) # Output: Meow!
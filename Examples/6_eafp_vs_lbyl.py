class Dog:
	def speak(self):
		return "Woof!"

class Car:
	def honk(self):
		return "Beep Beep!"

def animal_sound(animal):
	# We don't check the type of 'animal', just call speak()
	print(animal.speak())
	
# LBYL example
def lbyl_animal_sound(animal):
	if not hasattr(animal, "speak"):
		print("Object cannot speak!")
		return # return just to break from the function
	print(animal.speak())

# EAFP example
def eafp_animal_sound(animal):
	try:
		print(animal.speak())
	except AttributeError:
		print("Object cannot speak!")
		
dog = Dog()
car = Car()

lbyl_animal_sound(dog) # Otuputs: "Woof!" 
eafp_animal_sound(dog) # Outputs: "Woof!"
lbyl_animal_sound(car) # Otuputs: "Object cannot speak!" 
eafp_animal_sound(car) # Outputs: "Object cannot speak!"
class Car:
	def honk(self):
		return "Beep Beep!"

def animal_sound(animal):
	# We don't check the type of 'animal', just call speak()
	print(animal.speak())
	
car = Car()
animal_sound(car)
# Outputs:
# Traceback (most recent call last):
#   File "<python-input-0>", line 10, in <module>
#     animal_sound(car)
#     ~~~~~~~~~~~~^^^^^
#   File "<python-input-0>", line 7, in # animal_sound
#     print(animal.speak())
#           ^^^^^^^^^^^^
# AttributeError: 'Car' object has no attribute 'speak'
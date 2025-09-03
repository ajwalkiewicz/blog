"""
Data validation
"""

def greet(name, age):
	if not isinstance(name, str):
		raise ValueError(f"Name has to be str, got {type(name)}")
	if not isinstance(age, int):
		raise ValueError(f"Age has to be int, got {type(age)}")
	return f"Hello, {name}. You are {age} years old."

message = greet(30, "Alice")
#Traceback (most recent call last):
#  File "<python-input-2>", line 1, in <module>
#    greet(30, "Alice")
#    ~~~~~^^^^^^^^^^^^^
#  File "<python-input-0>", line 3, in greet
#    raise ValueError(f"Name has to be str, got {type(name)}")
#ValueError: Name has to be str, got <class 'int'>
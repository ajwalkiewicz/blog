"""
History - types are not needed
"""

def greet(name, age):
    return "Hello, " + name + " You are " + age + " years old."

message = greet("Alice", 30)


# Outputs:
# Traceback (most recent call last):
#   File "<python-input-1>", line 4, in <module>
#     message = greet("Alice", 30)
#   File "<python-input-1>", line 2, in greet
#     return "Hello, " + name + " You are " + age + " years old."
#            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
# TypeError: can only concatenate str (not "int") to str
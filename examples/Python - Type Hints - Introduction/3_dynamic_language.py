class Int(int):
    def __add__(self, value: int | str) -> str | int: # type: ignore
        if isinstance(value, str):
            return str(self) + value
        return super().__add__(value)
    
class Str(str):
    def __add__(self, value: int | str) -> str:
        if isinstance(value, int):
            return self + str(value)
        return super().__add__(value)
    
my_int = Int(5)
my_str = Str("Hello")

print("Is Int type of int:", isinstance(my_int, int)) 
print("Is Str type of str:", isinstance(my_str, str))

print("Type of Int:", type(my_int))
print("Type of Str:", type(my_str))

print("Adding Int to Int:", Int(5) + Int(5))
print("Adding Int to Str:", Int(5) + Str("World"))
print("Adding Str to Int:", Str("Hello") + Int(5))
print("Adding Str to Str:", Str("Hello") + Str("World"))

# Output:
# Is Int type of int: True
# Is Str type of str: True
# Adding Int to Int: 10
# Adding Int to Str: 5World
# Adding Str to Int: Hello5
# Adding Str to Str: HelloWorld
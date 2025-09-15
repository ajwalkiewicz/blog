---
title: Python - Type Hints - Introduction
description: My subjective introduction to Python type hints
date: 2025-09-02T22:55:17+00:00
draft: false
tags:
  - python
  - type-hints
---
# Intro

TODO

# History

When preparing to write this blog post, I decided to dig in a little bit about history of types. To my surprise something that I took for granted was not that obvious in computer science for a ling time.

According to [Arcane Sentiment](https://arcanesentiment.blogspot.com/) post, the term "type" was not introduced in programming languages until 1959 in Algol. First "type" like term occurs in 1956 in Fortran, but something that we now nowadays as types was there called "mode".

In 1967 Chris Strachey created an influential set of lectures "[Fundamental Concepts in Programming Languages](http://www.itu.dk/courses/BPRD/E2009/fundamental-1967.pdf‎)" where he talked about types.

And in 1968 James Morris, applied a [type theory](https://en.wikipedia.org/wiki/Type_theory) to the programming languages.

So now things are getting interesting. Because it appears that type theory is something old that precedes even computers for decades. Between 1902 and 1908 [Bertrand Russel](https://en.wikipedia.org/wiki/Bertrand_Russell) created a type theory for mathematics.  

Nowadays, type theory is a academic study about [types systems](https://en.wikipedia.org/wiki/Type_system). And the type system is the set of rules that creates a relation between type like (string, integer, float etc.) and the specific term - in case of programming language, variable, parameter, argument etc.

At the very and we have [data types](https://en.wikipedia.org/wiki/Data_type). Because I cannot paraphrase well what the data type is, here you have a quote from Wikipedia.

> In [computer science](https://en.wikipedia.org/wiki/Computer_science "Computer science") and [computer programming](https://en.wikipedia.org/wiki/Computer_programming "Computer programming"), a **data type** (or simply **type**) is a collection or grouping of [data values](https://en.wikipedia.org/wiki/Value_\(computer_science\) "Value (computer science)"), usually specified by a set of possible values, a set of allowed operations on these values, and/or a representation of these values as machine types.
> Source: https://en.wikipedia.org/wiki/Data_type

But what for us is the type, and why we need (or don't need) them at all.  Once the types got finally popular in programming languages they had few purposes. 

For example, lets look at this small C program:

```c
#include <stdio.h>

int main() {
    int smallInteger = 42; // declaring a small integer
    printf("Value: %d\n", smallInteger);
    return 0;
}
```

In memory it looks like this:

```
+----------+----------+----------+----------+
| byte 1   | byte 2   | byte 3   | byte 4   |
+----------+----------+----------+----------+
| 00000000 | 00000000 | 00000000 | 00101010 |
+----------+----------+----------+----------+
```

So knowing what data we needs to be stored, program can allocate a necessary amount of bytes for it. In this example it is for, but for longer integers it can be 8, 16, 32 or even 64 bytes. Back in a day, when resources in computers were very scarce it was very important.

Second reason of using types is operations safety. 

```python
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
```

Python throws an error because it does not know how to reasonably perform operation on adding a number "age" to the string". In other words, how to change the bytes in the memory so it stores the data correctly*.

\* That's not entirely true, more further in the article.

# Python - dynamically typed language

Programming languages traditionally divides on dynamically typed and statically typed languages. In dynamically typed languages the type of the variable is evaluated at runtime not before like it happens in statically typed languages.

Statically typed languages would not allow for such operation on the compilation level, because they would detect that there is a type mismatch and the operation cannot be permitted.

But Python works a little bit different. Not only it checks the type during the runtime, but also, it executes the code, and then throw error. The fact that in previous example, there is an error, is because the implementation of the `int` and `str` objects does not allow for such use case. But this comparison does not happen on the "type" level - as there is not such thing like internal type that needs to match. It happens because both `int` and `str` implements the `__add__` method, where it is checked during runtime if the type of the other object allows for addition. 

Purely academically, cause I see no practical usage of such case we can create our own `int` and `str` objects that allows for such behavior:

```python
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
# Type of Int: <class '__main__.Int'>
# Type of Str: <class '__main__.Str'>
# Adding Int to Int: 10
# Adding Int to Str: 5World
# Adding Str to Int: Hello5
# Adding Str to Str: HelloWorld
```

And that code works. We can see `my_int` is of type `Int` and `my_str` is of type `Str`. And we can perform addition between `Int` and `Str`.

## Duck typing

 > If it walks like a duck and it quacks like a duck it is a duck.
 
Duck typing is partially related with types. In python everything is an object. 

You should also know that when Python tries to access an attribute on an object it does also not care about that object type, only if that object has specified attribute.

For example in below code, when `animal.speak()` is being executed, Python search for the attribute with that name on the class, and if such exists it tries to call an object that is related with such attribute - in this case a method object.

```python
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
```

In this example it doesn't matter what class is being passed, as long as it implements `speak` method. We could create a `MagicCar` that implements `speak`, and it will work.

This might sounds crazy, but in fact it is the core feature of Python. It allows for a lot of flexibility. But it can be a problem, when the passed object does not have required method implemented.

## EAFP vs. LBYL

If we create a class `Car` that `honk` instead of `speak`, than we receive attribute error.

```python
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
```

How can we handle that? obviously, we could use type hints, and run static type checker so they show the error, but that is still ahead of us. Now we want to prevent errors during the runtime.

There are to approaches **EAFP** (Easier to ask forgiveness than permission) and **LBYL** (Look before you leap).

```python
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
```

**EAFP** is generally considered to be more *Pythonic*, due to dynamic nature of Python. But which approach to take depends, on the situation. Raising an error consumes more resources, but performing every-time check in if-statement, also takes some time. Generally the rule of thumb is, to use **EAFP** when we don't expect to raise often an exception, cause in such case we don't waste time on if-statement check, but it we expect a wrong type or object to be passed often, thus exception raise would consume a lot of resources, then it is better to use **LBYL** approach with if-statement check.

# Type hinting, type annotations, type checking and data validation.

Before talking more about types and type hinting, we need to do a small distinction of what are type hints, type annotations and type checking.

So type hinting refers to all sorts of information about the types in the program. Those can be (deprecated now) in line comments right next to the variable, parameter or function. But types also can be part of the documentation string - in python called "docstring". 

Annotations is the sub-type of the type hinting that refers only to the special syntax, where after a colon we write the type of the parameter or variable. And after an arrow symbol "->" and before the colon in the function to show what type it is returning. Because of that type hints and annotations are often used interchangeably. 

It is worth to mention that annotations were introduced in Python 3.5 with the famous [PEP-484](https://peps.python.org/pep-0484/)
![image](/posts/images/20250901085342.png)

Example of type hints and annotations.
```python
from typing import List, Optional

def multiply_elements(
    numbers: List[int],  # parameter with annotation only
    factor: Optional[int] = None  # parameter with annotation only
) -> List[int]:
    """
    Multiply each number in the list by a factor.

    Args:
        numbers (List[int]): List of integers to multiply.
        factor (Optional[int]): Multiplication factor. Defaults to 1 if None.

    Returns:
        List[int]: The list of multiplied numbers.
    """
    # Using inline type comments for local variables instead of annotations
    if factor is None:
        factor = 1  # type: int  # default factor set here

    result = [num * factor for num in numbers]
    return result
    
# Inline type comment for a variable before use
values = [1, 2, 3, 4]  # type: List[int]
multiplied = multiply_elements(values, factor=3)  # type: List[int]
print(multiplied)  # Output: [3, 6, 9, 12]
```

Type checking is a process of static analysis that verifies if the types are correctly written in the code. It does not impact the program runtime. Which means that program can fail the type check and still runs correctly.

Following program has wrong types but it will still work:

```python
# Someone confused types of name and age, and leave None as a return type
def greet(name: int, age: str) -> None:
    return f"Hello, {name}. You are {age} years old."

message = greet("Alice", 30)
print(message)  # Output: Hello, Alice. You are 30 years old.
```

Data validation is the runtime process where we are checking if the data in the input is of correct type.

```python
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
```

# Why to use type hints

We already know that types in Python does not affect the runtime. So some may ask a question why to bother and use type hints in Python if they are anyway ignored?

1. Better development experience.
   Modern IDE's can recognize types in our code and recommend possible methods:
![image](/posts/images/20250831142539.png)
2. Improved code readability
3. Less errors in the code (when combined with type checker)
4. Self documenting code
5. Easier refactors

Last but not least, because type hints are not impacting the runtime, it means that you don't need to add all the possible types since the beginning. You can gradually add types as your program evolves, or when upgrading a legacy code.

# Simple Types

Let's start with the simple types called built-ins. Or in other languages they may be know as primitives. Although it is convenient to thing about them as primitives, remember that everything in Python is an object! So it only helps imagination. They are not real primitives.  

Table 1.

| Type     | Description                                             |
| -------- | ------------------------------------------------------- |
| `int`    | integer                                                 |
| `float`  | floating point number                                   |
| `bool`   | boolean value (subclass of `int`)                       |
| `str`    | text, sequence of unicode codepoints                    |
| `bytes`  | 8-bit string, sequence of byte values                   |
| `object` | an arbitrary object (`object` is the common base class) |

Example:

```python
# Variables
age: int  # Type hint without value assignment
          # This creates only an entry in the __annotations__
          # dictionary, the variable does not exist!
# age = 25  # Value assigned later

# Functions
def greet(name: str, age: int) -> str:
    return f"Hello, {name}. You are {age} years old."

# Usage example:
message = greet("Alice", 30)
print(message)  # Output: Hello, Alice. You are 30 years old.
```

Type hinting variable before assigning a value to it, useful in some cases for example when unpacking:

```python
# Source: mypy.readthedocs.io
# for mypy to infer the type of "cs" from:
a, b, *cs = 1, 2  # error: Need type annotation for "cs"

rs: list[int]  # no assignment!
p, q, *rs = 1, 2  # OK
```

Annotating empty collections:

```python
# Source: mypy.readthedocs.io
l: list[int] = []       # Create empty list of int
d: dict[str, int] = {}  # Create empty dictionary (str -> int)
``` 

But `list` and `dict` are not on the list on our basic types. But before diving into beyond basic types, let's pause and talk about type checkers, as they are going to be very useful for us.

# Type checkers

Type checkers are the programs that read the code and validates if the types are correctly annotated. They are raising errors if there is something wrong. Their usage can help detect bugs in the code earlier, before running it.

## Popular Type checkers

MyPy is one of the oldest and most renowned type checker in the Python world. it can be considered as a golden standard.

In this article, I'm going to focuse and use only MyPy.

### [MyPy](https://www.mypy-lang.org/)

![image](/posts/images/20250831143608.png)

### [Pyright](https://microsoft.github.io/pyright/#/)

If you are using a Pylance extension in VS Code, then you are also using Pyright, maybe even without knowing it, vecause Pylance incorporates Pyright


![image](/posts/images/20250831143626.png)

### [ty](https://docs.astral.sh/ty/)

A new type checker, from Astral company, that gave us very good and popular tools lie `ruff` and `uv`

Still in beta, but I recommend to have an eye on it, cause if it will be as good as other their tools, it may become very popular in the future.

![image](/posts/images/20250831143645.png)

# Beyond basics

Going back to types, unfortunately in bigger programs it becomes quickly obvious that simple types are not enough. Fortunately Python provides a lot of generic types ready to use. 

### Generic Types

| Type                | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| `list[str]`         | list of `str` objects                                            |
| `tuple[int, int]`   | tuple of two `int` objects (`tuple[()]` is the empty tuple)      |
| `tuple[int, ...]`   | tuple of an arbitrary number of `int` objects                    |
| `dict[str, int]`    | dictionary from `str` keys to `int` values                       |
| `Iterable[int]`     | iterable object containing ints                                  |
| `Sequence[bool]`    | sequence of booleans (read-only)                                 |
| `Mapping[str, int]` | mapping from `str` keys to `int` values (read-only)              |
| `type[C]`           | type object of `C` (`C` is a class/type variable/union of types) |
Other popular generic types:
- `Callable`, 
- `Generator`

Generic types like `list`, `tuple` and `dict` are ready to use Immediately. Other ones, needs to be imported from [`collections.abc`](https://docs.python.org/3/library/collections.abc.html#module-collections.abc "(in Python v3.13)") module.

```python
from collections.abc import Callable, Iterable

def process_people(
	people: Iterable[tuple[str, int]],
	transform: Callable[[tuple[str, int]], tuple[str, int]],
) -> list[tuple[str, int]]:
	"""Applies the transform function on each person tuple and returns a dictionary
	with original and transformed lists."""
	return [transform(person) for person in people]

# Example usage:
people = [("Alice", 30), ("Bob", 25)]
def celebrate_birthday(person: tuple[str, int]) -> tuple[str, int]:
	name, age = person
	return (name, age + 1)

result = process_people(people, celebrate_birthday)
print(result)
```
It is worth to mention that before python 3.9, all of the generic types has to be imported from `typing` module, and `list`, `dict` and `tuple`, has to be imported as `List`, `Dict` and `Tuple`, with first letter capital.

### Aliases

We progress with our annotations, and we used more advanced generic types, but careful reader probably noticed, that `Callable[[tuple[str, int]], tuple[str, int]]` becomes actually less readable.

In such situations aliases comes handy.

Example:

```python
from collections.abc import Callable, Iterable

Person = tuple[str, int]

def process_people(
	people: Iterable[Person],
	transform: Callable[[Person], Person],
) -> list[Person]:
	"""Applies the transform function on each person tuple and returns a dictionary
	with original and transformed lists."""
	return [transform(person) for person in people]

people = [("Alice", 30), ("Bob", 25)]

def celebrate_birthday(person: Person) -> Person:
	name, age = person
	return (name, age + 1)

result = process_people(people, celebrate_birthday)
print(result)
```

In newer version of Python (>3.12):

```python
type Person = tuple[str, int]
```

And in Python 3.10, the `TypeAlias` was introduced:

```python
from typing import TypeAlias

Person: TypeAlias = tuple[str, int]
```

### Classes

But operating on tuples can be very limiting. To contain data (and behavior, but not in this example) classes are perfect.

We can make the code even more clear.

```python
from collections.abc import Callable, Iterable


class Person:
	def __init__(self, name: str, age: int) -> None:
		self.name = name
		self.age = age
	
	def __str__(self) -> str:
		return f"{type(self).__name__}(name={self.name}, age={self.age})"
		
	def __repr__(self) -> str:
		return self.__str__()

def process_people(
	people: Iterable[Person],
	transform: Callable[[Person], Person],
) -> list[Person]:
	"""Applies the transform function on each person tuple and returns a dictionary
	with original and transformed lists."""
	return [transform(person) for person in people]

people = (Person("Alice", 30), Person("Bob", 25)) # tuples are also Iterables!

def celebrate_birthday(person: Person) -> Person:
	person.age += 1
	return person

result = process_people(people, celebrate_birthday)
print(result)
```

### Dataclasses

To go one step further, we can change the `Person` class to the `dataclass`. Dataclasses are perfect for small objects that mostly encapsulate data. They give us very concise syntax, and under the hood add all the boilerplate for us. 

```python
from collections.abc import Callable, Iterable
from dataclasses import dataclass

@dataclass
class Person:
	name: str
	age: int

def process_people(
	people: Iterable[Person],
	transform: Callable[[Person], Person],
) -> list[Person]:
	"""Applies the transform function on each person tuple and returns a dictionary
	with original and transformed lists."""
	return [transform(person) for person in people]

people = [Person("Alice", 30), Person("Bob", 25)]

def celebrate_birthday(person: Person) -> Person:
	person.age += 1
	return person

result = process_people(people, celebrate_birthday)
print(result)
```

### Any

`Any` is a special type that can represents anything. Because of that everything is allowed to be done with Any. Anything can be assigned to Any, and Any can be assigned to anything. All methods, operations etc. are allowed on Any.

But be careful with Any, because it allows you to lie the type checkers. If used incorrectly, it can actually silence the issues, that can come up later as errors.

```python
from typing import Any

#Source: mypy.readthedocs.io
a: Any = None
s: str = ''
a = 2     # OK (assign "int" to "Any")
s = a     # OK (assign "Any" to "str")
```

Personally I find `Any` useful then you literally don't care about the content of the container object like `list`

```python
def get_len(it: list[Any]) -> int:
	return len(it)
```

The above example does not have much of a practical value, but it conveys the idea. In this case, it literally does not matter what kind of the objects are inside the `it` list.

### Unions and Optionals

Now, you already have a lot in you type hints arsenal. But what if you need something more unique, or what if argument passed to the function can be one of more types.

Here, unions and optionals comes handy.

```python
def find_person(people: Iterable[Person], name: str) -> Person | None:
    for person in people:
        if person.name == name:
            return person

def greet_person(person: Person, greeting: str | None = None) -> str:
    if greeting is None:
        greeting = "Hello"
    return f"{greeting}, {person.name}!"
```

Before python 3.10, you can find an older syntax:

```python
from typing import Union, Optional

def find_person(people: Iterable[Person], name: str) -> Union[Person, None]: 
	...
	
def greet_person(person: Person, greeting: Optional[str] = None) -> str: 
	...
```

### Ellipsis

In the example above you may drag attention for `...` three dots that are in the function bodies.
Three dots is a special syntax for `Ellipsis` object.

It's a special object in Python that does nothing. it is only one in the Python program (similar to `None`) and it is common to see it in the examples, or in the stub files. 

Python syntax requires to put something into function or class body, when want to create a function or class without defining it's body and without syntax error, you can use `Ellipsis`.

The main difference between `Ellipsis` and `pass` keyword is that. `Ellipsis` is the object and `pass` is a keyword, that allows to skip function or class body.

Whether to use `pass` or `Ellipsis` is often up to your personal preferences. Unfortunately, except stub files there is no guideline when to use which. The most important is to be consequent in the usage, and if you are mixing bot of them, then add guideline to your project explaining when do you use each one.

Besides example, and empty functions or classes `Ellipsis` has one more practical usage in type hints.

In the container types like, `tuple` it can indicate that the tuple is of unspecified lenght of certain types.

```python
# This means that the people is a tuple with just ONE element of type Person.
# Othen it is not what we want'
people: tuple[Person] 

# Now this means that the people is a tuple with unspecified numbered of elements.
# But all of those elements are of type Person
people: tuple[Person, ...] 
```

We can also use `Ellipsis` in the `Callable` to specify the unknown number of arguments that callable accepts.

```python
def handle_person_action(action: Callable[..., None], person: Person) -> None:
    action(person)

def greet(person: Person) -> None:
    print(f"Hello, {person.name}!")

person = Person("Alice", 30)

# Using the handler with different callables
handle_person_action(greet, person) # Outputs: Hello, Alice!
handle_person_action(lambda x: print(f"Person is {x.name}"), person) # Outputs: Person is Alice
```

TODO:  Always use general types  as inputs and return as much specific types whenever possible.

# Generics

You know already generic types like `lits`, `tuple`, `dict`, `Iterable`, `Callable` etc. But what if you would like to create your own generic type? 

Python has support for that. You can create a generic function, that accepts generic type:

```python
from typing import TypeVar

T = TypeVar('T') # We define a generic variable

def get_first_element(items: list[T]) -> T:
	return items[0]

print(get_first_element([1, 2, 3])) # Output: 1
print(get_first_element(["apple", "banana", "cherry"])) # Output: apple
```

Or even generic class:

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Box(Generic[T]):
	def __init__(self, content: T):
		self.content = content

	def get_content(self) -> T:
		return self.content

int_box = Box[int](123)
print(int_box.get_content()) # Output: 123

str_box = Box[str]("Hello")
print(str_box.get_content()) # Output: Hello
```

In python 3.12 and above you can find a newer syntax:

```python
def get_first_element[T](items: list[T]) -> T: ...

class Box(Generic[T]): ...
```

# Abstract Base Classes

In Python, **Abstract Base Classes (ABCs)** are similar to other languages, like Java, but at the same time they differ a lot. They allows to create a base class, that cannot be instantiated, it can only be used as a parent class for other classes. But just like regular classes sub-classes of an abstract class inherits all of its attributes. In a way they are like interfaces, where we define what methods needs to be implemented by the sub-class.

Sub-classes of an abstract class have to implement methods that are decorated with `@abstractmethod` in the abstract class. If a sub-class doesn't implement it becomes an abstract class itself. 

What may be different from other languages, is that abstract class, can share it's logic with the sub-classes, define regular not abstract methods, and even allows to call and execute methods with abstract method decorator to be called from sub-classes (tough not recommended).

A simple example will make it more clear. 

```python
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
```

I used this code initially, to show duck typing. Here we still are using duck typing, but with Abstract Base Class we can annotate, an `animal` parameter in the `animal_sound` function that is it a type of `Animal`. Now type checkers like mypy, will check if the object passed to the function is of the correct type, thus if it has `speak` method.

# Protocols

Protocols uses something that professionally is called "Structural Sub-typing". That means checking if an object conforms a structure.

There is not need for inheritance! Because of that Protocols gives you a lot of flexibility.

```python
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
```

`Speaker` defines method `speak`, but it contains only its signature (i.e. its name, parameters with types and what type it returns). In the body of the function there is only `Ellipsis`.

Similarly like with ABC's, type checkers, now will check if the object passed to the `talk` function has `speak` method. If it has it will be considered as a sub-class of the `Speaker` and thus a valid type.

# ABC vs Protocols

When to use which? As usually there is no strict simple answer for that. Here I can only tell you my opinion about some pros and cons of bother and when I prefer to use one over the other. 

Abstract base classes in a very explicit way force other developers to follow the interface that they define. I find it very useful when using them for internal parts of an application that are not going to be exposed for others i.e. as a library. Because if you are writing a library that others import and use as a third party dependency, then protocols are much better fit. You usually don't want to make others to inherit from some internal abstract classes so they code could pass a type check. 

Protocols are also good if you want to define attributes on the class. 

If you need to use `isinstance` than you need to add decorator to the protocol class `@runtime_checkable` but even python documentation warns that this is not safe method:

![image](/posts/images/20250903104653.png)

As an extra, there is nothing to stop us to combine ABC and protocols in same class:

```python
import abc
import typing

class Config(typing.Protocol):
	name: str

class Platform(abc.ABC):
	config = Config

	def __init_subclass__(cls, /, config: type[Config], **kwargs):
		super().__init_subclass__(**kwargs)
		cls.config = config

	@abc.abstractmethod
	def get_name(self) -> str:
		...

class SonyConfig:
	name = "Sony"

class Sony(Platform, config=SonyConfig):
	def get_name(self) -> str:
		return self.config.name

if __name__ == "__main__":
	sony = Sony()
	name = sony.get_name()
	print(name)
```

# Problems

## Type Hints don't impact runtime, ... right?

![image](/posts/images/20250913091040.png)

I heard that so many times, that I started to believe that. And in a way it is true. Indeed types does not impact run time, as they don't matter for Python interpreter. This is something that I was trying to explain with the custom `Int` and `Str` classes at the beginning. 

So where's the problem? Python is constructed in a way that everything after a colon in the function signature, in the parameters is a valid python code that can be evaluated. That means things there can break on the evaluation level.

```python
def create_message(person: Person | None = None) -> str:
	if person is None:
		return "Generic message to everyone"
	
	return f"Personalized message to {person.name}"

class Person: ...
```

This example fails, because we are trying to use object `Person` that is yet not defined. Python is an interpreted language after all, and when the interpreter reads the signature of `create_message` function it does know nothing about `Person`

```
NameError: name 'Person' is not defined
```

There are 2 solution for that. First we can just move `create_message` below definition of `Person` class. but sometimes we cannot or don't want to do that. That's why there is second way to use string literal as a type. When using string literals, type checkers and IDE's still understand that it is `Person` object type, and at the same time for interpreter it is just a string, so it won't complain about `NameError`

```python
def create_message(person: "Person" | None = None) -> str:
	if person is None:
		return "Generic message to everyone"
	
	return f"Personalized message to {person.name}"

class Person: ...
```

But now we hit another issue, that personally I'm committing quite often. A union operator `|` cannot operate between string and another object!

```
TypeError: unsupported operand type(s) for |: 'str' and 'NoneType'
```

So as you can see, types hints don't not affect runtime, until they do.

The solution for this is to either put everything into string, or use an old `Union` type.

```python
def create_message(person: "Person | None" = None) -> str: ...

from typing import Union
def create_message(person: Union["Person", None] = None) -> str: ...
```

## Future

There is special module in python called `__future__`, it is rarely used, but sometimes it is useful. Creators of Python put there features that may alternate the standard behavior of python. One of those features is `annotations`.

```python
from __future__ import annotations
```

When above line appears at the very top of the imports, it changes the behavior of Python and how it evaluate annotations. Now all annotations becomes strings!

OK, cool, but why would anyone use it? In a bigger projects when packages import objects one from another, it is easy to fall into the issue with circular imports. In a naive example, when module `A` imports function `b` from module `B`, and module `B` imports function `a` from module `A`, we get a circular import error.

This looks like this:
```
A -> b (from B) -> a (from A) Error!
```

Such imports are rather easy to find even before running the code. That's why usually, circular imports happens in bigger projects where it's harder to track such dependencies:

```
A -> b (from B) -> c (from C) -> d (from D) -> b (from B)
```
It can be even more difficult and annoying when we import things in the package `__init__.py` file. 

One way to solve that issue (there are more but this is not article about circular imports) is to use `TYPE_CHECKING` constant. often we import things only for annotations, we do not use them in any other way. `TYPE_CHECKING` is a special variable that is set to true only when type checkers are validating the code. So we can put the import behind the type check:

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from people import Person

def create_message(person: Person | None = None) -> str: ...
```

But now we got:

```
NameError: name 'Person' is not defined
```

Because, we import `Person` only for type checks, during the run time this code is being evaluated and Python does not see the `Person` in the scope.

That's why we wan't to use `from __future__ import annotations`, because, now even during the run time, it will be just a string literal that does nothing at the runtime.

```python
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from people import Person

def create_message(person: Person | None = None) -> str: ...
```

# Other typing features

Many of the following features are not available in older versions of python. but There is a way to use them. Package [typing_extensions](https://pypi.org/project/typing-extensions/) was created to support new tying features in older python versions. 

## Overload

Better annotations when types becomes more complex. Sometimes methods can return different types, depends on what arguments are passed. In the below example, `get_info` method can return either string, integer or tuple of string and integer. But the logic of the function clearly makes distinction what types will be returned depends what arguments are passed. 

Overloading allows you to narrow down types, and make it more precise. 

```python
from typing import overload, Literal, Union, Tuple, Self

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

    # Overloads for better type hints
    @overload
    def get_info(self, detail: Literal["name"]) -> str: ...
    @overload
    def get_info(self, detail: Literal["age"]) -> int: ...
    @overload
    def get_info(self) -> Tuple[str, int]: ...

    # Actual implementation (only one real function)
    def get_info(self, detail: Union[Literal["name"], Literal["age"], None] = None) -> Union[str, int, Tuple[str, int]]:
        if detail == "name":
            return self.name
        elif detail == "age":
            return self.age
        else:
            return (self.name, self.age)

person = Person("Alice", 30)

print(person.get_info())          # Outputs: ('Alice', 30)
print(person.get_info("name"))    # Outputs: 'Alice'
print(person.get_info("age"))     # Outputs: 30
```

## Override

For extra safety,  you can use `@override` decorator. It has couple benefits. First it protects you from typos, which can actually leads to some unexpected an hard to find bugs, because you class still will be working, but the method that you think is being called, is not. Instead Python will be using a method from the parent class. 

Apart from typos, it also automatically documents you code, and make it for others easier to understand. I know that there are IDE's like [PyCharm](https://www.jetbrains.com/pycharm), that actually can gives you same information, but that tights you to usage of a specific IDE, and people are using various of code editors for their work. Plus with decorator you can add `MyPy` or other type checker to your CI process. 

```python
import abc
from typing import override

class Animal(abc.ABC):
	@abstractmethod
	def speak(self) -> str: ...

class Dog(Animal):
	@override
	def speak(self) ->str: ...

class Cat(Animal):
	def speak(self) -> str: ... # Error! (becasue we didn't use @override)
	
class Fish(Animal):
	@override
	def speek(self) -> str: ... # Error! (because of typo in speak)
```

But that doesn't work by default. You need to set specific type checker settings or add an extra flag like [`--enable-error-code explicit-override`](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-enable-error-code) or [`--strict`](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-strict)

## Self

A convenient way of annotating that method returns instance itself. 

```python
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
```

It was introduced in Python 3.11.  Before `Self` to achieve the same thing you need to use a string literal:

```python
class Person:
	def __init__(self, name: str, age: int) -> None: ...
	def __str__(self) -> str: ...

	def celebrate_birthday(self) -> "Person": ...
	
	def change_name(self, new_name: str) -> "Person": ...
```

# MyPy Misc

## Cast

Cast is another way to trick MyPy to think that certain expression is of specific type. You have to be very careful when using it, because YOU are telling MyPy what is the type, and if you make a mistake in type, MyPy will not catch it. Important to mention `cast` unlike in other languages, does not change value from one type to the other, for example integer won't be converted to string, even implicitly (:wink: to JS) 

I find it useful everywhere where you as a human knows by the power of the logic that something HAS to be of a specific type, but MyPy doesn't. For example when using `or` operator in the old fashion manner as a replacement for ternary operator.  

```python
# Source: https://mypy.readthedocs.io/en/stable/type_narrowing.html#limitations
from typing import cast

class C:
    pass

def f(a: C | None, b: C | None) -> C:
    if a is not None or b is not None:
        # return a or b         # Incompatible return value type (got "C | None", expected "C")
        return cast(C, a or b)  # Type narrowed to C, because as a human I can 
                                # understand that this has to be C
    return C()
```

In the above example, as humans we know that function `f` has to return object `C`. But MyPy cannot understand the logic there and thinks that it can be `C` or `None`. Using cast force MyPy to think that only `C` can be returned.

Cast can also be useful when dealing with external API's or libraries that does not support fully types of can't support them, like `request.json` cannot possibly know what types in the returned JSON are.

```python
# Source: https://swapi.info
import requests

url = "https://swapi.info/api/starships/12"
response = requests.get(url)
starship = response.json()
print("Cost: ", starship["cost_in_credits"] / 1000)
```

Without extra annotation, `starship` is a type of `Any`. Which is a little bit problematic, MyPy won't throw any errors, because as we know all operations are allowed on `Any`. Without reading the API documentation, someone could think that  `cost_in_credits` returns a number, but in fact that API returns everything as string.

```
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

Solution for that can be usage o either annotating `starship` variable or usage of cast:

```python
starship: dict[str, str] = response.json()
# OR
starship = cast(dict[str, str], response.json())
```

Although for production code, I would actually recommend using [Pydantic](https://docs.pydantic.dev/latest/) models. They give you better annotation, especially in API that can return various types, and they give you option for validation. Plus they give you tons of other benefits, but that's the material for another article. 

## Flags
- [`--disallow-untyped-defs`](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-disallow-untyped-defs)
- [`--enable-error-code explicit-override`](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-enable-error-code)
- `--strict`

## ignore

TODO

# References

General
- Type Theory: https://en.wikipedia.org/wiki/Type_theory
- Type System: https://en.wikipedia.org/wiki/Type_system
- Data Type: https://en.wikipedia.org/wiki/Data_type
- A brief history of "type": https://arcanesentiment.blogspot.com/2015/01/a-brief-history-of-type.html

Python
- PEP-484: https://peps.python.org/pep-0484/
- Static Typing with Python: https://typing.python.org/en/latest/#
- Python typing module: https://docs.python.org/3/library/typing.html
- Python Data Model: https://docs.python.org/3/reference/datamodel.html
- Mypy docs: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
- FastAPI Python types: https://fastapi.tiangolo.com/python-types
- RealPython Type Checking: https://realpython.com/python-type-checking
- Lazy annotations: https://realpython.com/python-annotations/
- EAFP vs LBYL: https://realpython.com/python-lbyl-vs-eafp/

YouTube Videos
- [Python Tutorial: Type Hints - From Basic Annotations to Advanced Generics](https://www.youtube.com/watch?v=RwH2UzC2rIo)
- [Python Tutorial: Duck Typing and Asking Forgiveness, Not Permission (EAFP)](https://www.youtube.com/watch?v=x3v9zMX1s4s)
- [PyWaw #117 What NOT TO DO when type hinting in Python?](https://www.youtube.com/watch?v=4y-8wokSpfM&t) 

Examples:
- 
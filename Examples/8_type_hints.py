"""
Annotations are optional
"""

# Someone confused types of name and age, and leave None as a return type
def greet(name: int, age: str) -> None:
    return f"Hello, {name}. You are {age} years old."

message = greet("Alice", 30)
print(message)  # Output: Hello, Alice. You are 30 years old.
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
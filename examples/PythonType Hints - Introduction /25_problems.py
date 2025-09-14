from dataclasses import dataclass

def create_message(person: "Person" | None = None) -> str:
	if person is None:
		return "Generic message to everyone"
	
	return f"Personalized message to {person.name}"

@dataclass
class Person:
	name: str
	age: int

# TypeError: unsupported operand type(s) for |: 'str' and 'NoneType'

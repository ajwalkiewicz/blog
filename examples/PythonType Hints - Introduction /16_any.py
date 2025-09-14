from typing import Any

#Source: mypy.readthedocs.io
a: Any = None
s: str = ''
a = 2     # OK (assign "int" to "Any")
s = a     # OK (assign "Any" to "str")

# Good use of Any
def get_len(it: list[Any]) -> int:
	return len(it)

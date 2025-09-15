"""
Example of type hints
"""

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
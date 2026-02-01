import pdb
from typing import List

def even_sum(numbers: List[int]) -> int:
    """
    Calculate the sum of even numbers in a list.

    Args:
        numbers (List[int]): List of integers.

    Returns:
        int: Sum of even numbers.
    """
    if not numbers:
        raise ValueError("The list is empty")  # Error handling for empty list

    total = sum(num for num in numbers if num % 2 == 0)  # List comprehension for clarity
    return total

# Data
nums = [10, 15, 20, 25, 30]

# Debugging checkpoint
pdb.set_trace()  # Inspect variables and execution flow here

# Function call
try:
    result = even_sum(nums)
    print(f"Even numbers ka sum = {result}")
except ValueError as e:
    print(f"Error: {e}")
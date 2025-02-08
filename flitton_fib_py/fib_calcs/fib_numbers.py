from typing import List
from .fib_numbers import recurring_fibonacci_nuber 
def calculate_numbers(numbers:List[int]) -> List[int]:
     return [recurring_fibonacci_nuber (number=i)] for i in numbers
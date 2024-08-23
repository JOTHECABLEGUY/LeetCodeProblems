from time import perf_counter
import sys
from functools import lru_cache
import re
@lru_cache()
def fib(num:int): # 1, 1, 2, 3
    """
    Compute the Fibonacci number at a given index using memoization.

    This function returns the Fibonacci number corresponding to the specified index. 
    It utilizes caching to optimize performance, allowing for efficient computation even for larger indices.

    Args:
        num (int): The index of the Fibonacci number to compute, where the sequence starts with fib(0) = 0 and fib(1) = 1.

    Returns:
        int: The Fibonacci number at the specified index.
    """
    return num if num <= 1 else fib(num-1) + fib(num-2)
def main():
    target_number_index = sys.argv[1] if len(sys.argv) > 1 else "50"
    if not re.match(r"\d+", target_number_index):
        raise ValueError("Invalid value, must enter a whole number >= 0")
    target_number_index = int(target_number_index)
    start = perf_counter()
    print(fib(target_number_index))
    print(f"time taken: {perf_counter()-start:.4f} seconds")
if __name__ == "__main__":
    main()
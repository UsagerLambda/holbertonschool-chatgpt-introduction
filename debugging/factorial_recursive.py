#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculate the factorial of a number using recursion.
    
    Parameters:
    - n (int): The number for which to calculate the factorial.
    Must be a non-negative integer.
    
    Returns:
    int: The factorial of the number 'n'.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)



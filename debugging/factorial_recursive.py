#!/usr/bin/python3 # Shebang line to specify the Python 3 interpreter
import sys # Import the sys module to access command-line arguments

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
    n (int): The non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the number n. If n is 0, it returns 1 as 0! is 1.
    """
    if n == 0: # Base case: the factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1) # Recursive case: the factorial of n is n * factorial(n-1)

# Get the first command-line argument (the number to calculate the factorial for)
f = factorial(int(sys.argv[1]))
print(f) # Print the calculated factorial


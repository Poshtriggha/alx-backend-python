#!/usr/bin/env python3
"""
Module to define a function add that takes 
two float arguments and returns their sum.
"""

def add(a: float, b: float) -> float:
    """
    Function to add two floats.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b

if __name__ == "__main__":
    print(add(1.11, 2.22) == 1.11 + 2.22)

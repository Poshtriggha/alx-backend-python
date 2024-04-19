#!/usr/bin/env python3
"""
Module to define a function make_multiplier.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function to create a multiplier function.

    """
    def multiplier_function(x: float) -> float:
        """
        Inner function to perform multiplication.

        Args:
            x (float): The number to multiply.

        Returns:
            float: The result of the multiplication.
        """
        return x * multiplier
    
    return multiplier_function

if __name__ == "__main__":
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))

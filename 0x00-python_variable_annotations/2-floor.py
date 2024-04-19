#!/usr/bin/env python3
"""
Module to define a function 
"""

import math

def floor(n: float) -> int:
    """
    Function to return the floor of a float.

    """
    return math.floor(n)

if __name__ == "__main__":
    ans = floor(3.14)
    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))

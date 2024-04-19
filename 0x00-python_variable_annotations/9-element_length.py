#!/usr/bin/env python3
"""
Module to define a function element_length.
"""

from typing import Iterable, Sequence, Tuple, List

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function to calculate the length of elements in a list.

    """
    return [(i, len(i)) for i in lst]

if __name__ == "__main__":
    print(element_length.__annotations__)

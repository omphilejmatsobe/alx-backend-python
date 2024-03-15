#!/usr/bin/env python3
"""
    Duck type and iteration
"""
from typing import Tuple, Sequence, List, Iterable, Union


def element_length(lst: Iterable[Sequence])\
        -> List[Tuple[Sequence, int]]:
    """
        Args:
            lst: Sequence of list

        Return:
            List of tuple of sequence of integers
    """

    return [(x, len(x)) for x in lst]

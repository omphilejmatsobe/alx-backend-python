#!/usr/bin/env python3
"""
    Module  of integers and floats and returns their sum as a
    float.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Args:
            _list: float-int numbers

        Return:
            float base in int or float numbers
    """

    result: float = 0

    for x in mxd_lst:
        result += x

    return result

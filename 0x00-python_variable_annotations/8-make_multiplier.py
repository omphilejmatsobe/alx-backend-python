#!/usr/bin/env python3
"""
    Module with  function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Args:
            multiplier: factor

        Return:
            multiplication in float
    """

    def x(f: float) -> float:
        """ Get the second argument somthing like JS """
        return float(f * multiplier)

    return x

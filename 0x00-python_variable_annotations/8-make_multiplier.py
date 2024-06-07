#!/usr/bin/env python3
"""this module contain function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
      desc:
        takes a float multiplier as argument and returns a function
        that multiplies a float by multiplier.
      args:
        multiplier: float
      return:
        function
    """
    return lambda a: a * multiplier

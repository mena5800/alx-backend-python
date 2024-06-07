#!/usr/bin/env python3
"""this module contain function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
      desc:
        takes a string k and an int OR float v as arguments and
        returns a tuple.
        The first element of the tuple is the string k.
        The second element is the square of the int/float v
        and should be annotated as a float.
      args:
        k: string
        v: int or float
      return:
        tuple contain k and v
    """
    return (k, v ** 2)

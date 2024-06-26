#!/usr/bin/env python3
"""this module contain function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
      desc:
        takes a list input_list of floats as argument and
        returns their sum as a float.
      args:
        input_list : list of float numbers
      return:
        sum of list
    """
    return sum(input_list)

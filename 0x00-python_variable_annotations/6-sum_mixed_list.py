#!/usr/bin/env python3
"""this module contain function sum_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
      desc:
        takes a list mxd_lst of integers and floats and
        returns their sum as a float.
      args:
        mxd_lst : list of float and int
      return:
        sum of list
    """
    return sum(mxd_lst)

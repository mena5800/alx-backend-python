#!/usr/bin/env python3
"""this module contain function make_multiplier"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate the below function’s parameters and return values
    with the appropriate types"""
    return [(i, len(i)) for i in lst]

#!/usr/bin/env python3

"""Complex types - list of floats"""
from typing import List


def sum_list(sum_list: List[float]) -> float:
    """Returns the sum of list as a float"""
    total: float = 0
    r = [total := total + x for x in sum_list]
    return r[2]

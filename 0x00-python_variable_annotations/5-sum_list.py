#!/usr/bin/env python3
"""Annotated sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes list of floats and returns their sum as float"""
    a: float = 0.0
    for i in input_list:
        a += i
    return a

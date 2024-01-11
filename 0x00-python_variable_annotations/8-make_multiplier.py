#!/usr/bin/env python3
"""Type-annotated make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes float & return function that multiplies the float"""
    return lambda x: x * multiplier

#!/usr/bin/env python3
"""Type annotated to_kv"""
from typing import Union, Tuple
from math import sqrt


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Taes string & float/int & return string & float tuple."""
    x = v ** 2
    return (k, x)

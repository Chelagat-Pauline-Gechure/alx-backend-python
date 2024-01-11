#!/usr/bin/env python3
"""Duck typed function"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes sequence & returns tuples of sequence and int"""
    return [(i, len(i)) for i in lst]

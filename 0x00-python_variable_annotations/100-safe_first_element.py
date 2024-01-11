#!/usr/bin/env python3
"""Duck typed function"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Input elements are not known"""
    if lst:
        return lst[0]
    else:
        return None

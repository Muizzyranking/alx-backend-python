#!/usr/bin/env python3
"""Anonnatation for a list of elements"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Anonnatation for a list of elements"""
    return [(i, len(i)) for i in lst]

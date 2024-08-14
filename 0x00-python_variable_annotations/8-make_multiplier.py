#!/usr/bin/env python3
"""Module for make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that takes a multiplier and returns a function"""
    def multiply(x: float):
        return x * multiplier
    return multiply

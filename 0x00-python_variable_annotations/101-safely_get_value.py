#!/usr/bin/env python3
""" Annotate the below function’s parameters and return
values with the appropriate types
"""

from typing import Mapping, Any, TypeVar, Union, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Safely returns the value for a given key from a dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default

#!/usr/bin/env python3
"""
This module contains a coroutine called
`async_generator` which yields random numbers.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that yields a
    random float between 0 and 10.

    Returns:
        AsyncGenerator[float, None]: An asynchronous generator
        that yields random floats.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        # yield random.random() * 10
        yield random.uniform(0, 10)

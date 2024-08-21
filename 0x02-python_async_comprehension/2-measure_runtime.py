#!/usr/bin/env python3
"""
This module contains a coroutine `measure_runtime` which
executes `async_comprehension` four times in parallel
and measures the total runtime.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes `async_comprehension` four times in parallel
    and measures the total runtime.

    Returns:
        float: The total runtime in seconds.
    """
    start_perf = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_perf = time.perf_counter()
    return (end_perf - start_perf)

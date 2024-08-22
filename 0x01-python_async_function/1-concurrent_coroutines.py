#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine
that spawns multiple `wait_random` tasks.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns `wait_random`
    `n` times with a specified `max_delay`.

    Parameters:
    n (int): The number of times to call `wait_random`.
    max_delay (int): The maximum delay in seconds
    for each `wait_random` call.

    Returns:
    List[float]: A list of all the delays in ascending order.
    """
    # Create a list to store the created tasks
    tasks = []
    # Create a list to store the results (delays) of the tasks
    delays = []

    # Create `n` tasks sequentially and store them in a list
    for i in range(n):
        # Create a task and append it to the tasks list
        task = wait_random(max_delay)
        tasks.append(task)

    # Execute tasks concurrently and gather their results sequentially
    for task in asyncio.as_completed(tasks):
        # Wait for the task to complete and
        # append the result to the delays list
        delay = await task
        delays.append(delay)

    # Return the list of delays
    return delays

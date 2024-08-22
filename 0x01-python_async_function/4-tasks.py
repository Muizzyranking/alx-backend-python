#!/usr/bin/env python3
"""
This module provides a function to create
multiple asyncio Tasks from task_wait_random.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates multiple asyncio Tasks for
    task_wait_random with the given n and max_delay.
    Waits for all Tasks to complete and
    returns a list of delays in ascending order.

    Parameters:
    n (int): The number of tasks to create.
    max_delay (int): The maximum delay in seconds for each task.

    Returns:
    List[float]: A list of all the delays in ascending order.
    """
    # Create an empty list to store tasks
    tasks = []
    # Create an empty list to store delays
    delays = []

    # Create tasks sequentially and append them to the tasks list
    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    # Execute tasks concurrently and gather their results sequentially
    for task in asyncio.as_completed(tasks):
        # Wait for the task to complete and
        # append the result to the delays list
        delay = await task
        delays.append(delay)

    # Return the list of delays
    return delays

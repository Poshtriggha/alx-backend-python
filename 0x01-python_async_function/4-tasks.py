#!/usr/bin/env python3
""" Module defining an asynchronous coroutine """

import asyncio
from typing import List

# Importing task_wait_random from module '3-tasks'
wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(number: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine task_wait_n.

    Spawns wait_random `number` times with the specified `max_delay`.
    
    Args:
        number (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for each wait_random call.
        
    Returns:
        List[float]: List of delays (float values) in ascending order.
    """
    # List to store the tasks
    tasks = [wait_random(max_delay) for _ in range(number)]
    
    # List to store the delays
    delays = []
    
    # Await for each task to complete
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays

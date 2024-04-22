#!/usr/bin/env python3
""" Module containing an asynchronous coroutine """

import asyncio
from typing import List

# Importing wait_random coroutine from a separate file
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(number: int, max_delay: int) -> List[float]:
    '''
    Asynchronously spawns wait_random `number` times with the specified `max_delay`.
    
    '''

    tasks = [wait_random(max_delay) for _ in range(number)]
    

    delays = []
    

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays

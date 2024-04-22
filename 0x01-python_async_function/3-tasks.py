#!/usr/bin/env python3
"""Module for an asynchronous coroutine"""

import asyncio

# Importing wait_random coroutine from a separate file without adjustment
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    ''' Function to create a task for wait_random coroutine '''
    return asyncio.create_task(wait_random(max_delay))

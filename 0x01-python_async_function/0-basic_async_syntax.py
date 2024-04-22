#!/usr/bin/env python3
"""
Module defining an asynchronous coroutine
"""

import asyncio
import random

async def generate_random_delay(maximum_delay: int = 10) -> float:
    """
    Asynchronous coroutine generate_random_delay takes an integer argument
    (maximum_delay, defaulting to 10)
    """
    random_delay = random.uniform(0, maximum_delay)
    await asyncio.sleep(random_delay)
    return random_delay

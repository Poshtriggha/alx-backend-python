#!/usr/bin/env python3
"""
Async generator module
"""

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously yields random numbers between 0 and 10 for 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

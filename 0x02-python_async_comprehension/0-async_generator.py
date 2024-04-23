#!/usr/bin/env python3
"""
Async generator module
"""

import asyncio
import random

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously yields random numbers between 0 and 10 for 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

async def print_yielded_values() -> None:
    """
    Asynchronously prints the values yielded by async_generator.
    """
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

if __name__ == "__main__":
    asyncio.run(print_yielded_values())

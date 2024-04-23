#!/usr/bin/env python3
"""
Async comprehension module
"""

import asyncio
from typing import List

async def async_comprehension() -> List[float]:
    """
    Asynchronously collects 10 random numbers using async comprehension over async_generator.
    """
    return [i async for i in async_generator()]

if __name__ == "__main__":
    asyncio.run(async_comprehension())

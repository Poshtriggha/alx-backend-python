#!/usr/bin/env python3
"""
Measure runtime module
"""

import asyncio
import time

async def measure_runtime() -> float:
    """
    Measures the total runtime.
    """
    start_time = time.time()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()

    return end_time - start_time

if __name__ == "__main__":
    print(asyncio.run(measure_runtime()))

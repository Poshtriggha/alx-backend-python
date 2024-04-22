#!/usr/bin/env python3
"""
Module on an asynchronous coroutine
"""

import asyncio
import random

async def wait_random(max_delay=10):
    await asyncio.sleep(random.uniform(0, max_delay))
    return max_delay

# Test cases
async def main():
    print(await wait_random())
    print(await wait_random(5))
    print(await wait_random(15))

if __name__ == "__main__":
    asyncio.run(main())

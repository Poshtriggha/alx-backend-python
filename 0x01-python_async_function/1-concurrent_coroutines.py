import asyncio
import random
from typing import List
from basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays

# Test cases
async def main():
    print(await wait_n(5, 5))
    print(await wait_n(10, 7))
    print(await wait_n(10, 0))

if __name__ == "__main__":
    asyncio.run(main())

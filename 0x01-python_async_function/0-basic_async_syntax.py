import asyncio
import random
from typing import List

async def wait_random(max_delay: int = 10) -> List[float]:
    await asyncio.sleep(random.uniform(0, max_delay))
    return [max_delay]

# Test cases
async def main() -> None:
    print(await wait_random())
    print(await wait_random(5))
    print(await wait_random(15))

if __name__ == "__main__":
    asyncio.run(main())

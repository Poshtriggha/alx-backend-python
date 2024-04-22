#!/usr/bin/env python3
""" AAA """

import asyncio
from typing import List
wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' AAA '''
    wait_times = []
    delays = []
    for _ in range(n):
        wait_times.append(wait_random(max_delay))

    for wait_time in asyncio.as_completed(wait_times):
        delay = await wait_time
        delays.append(delay)
    return delays
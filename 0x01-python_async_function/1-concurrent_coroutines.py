#!/usr/bin/env python3

"""
routine called that takes in int arguments and returns list of
all the delays from wait_random
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    returns the list of all the delays (float values)
    """

    delays: List[float] = []
    all_delays: List[float] = []

    for i in range(n):
        delays.append(wait_random(max_delay))

    for i in asyncio.as_completed(delays):
        result = await i
        all_delays.append(result)

    return all_delays

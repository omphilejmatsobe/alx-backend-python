#!/usr/bin/env python3

"""
Module with asynchronous coroutine that takes in an integer argument that
waits for a random delay between 0 and max_delay
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ takes in an integer argument that waits
        for a random delay between 0 and max_delay (included and float value)
        seconds and eventually returns it."""

    _random = random.uniform(0, max_delay)
    await asyncio.sleep(_random)
    return _random

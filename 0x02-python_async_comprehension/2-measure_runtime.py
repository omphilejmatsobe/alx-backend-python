#!/usr/bin/env python3
""" 
    Coroutine that executes async_comprehension four times
    in parallel using asyncio.
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measures the total runtime and returns it"""

    tasks = []
    intTime = time.time()

    for i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)
    finalTime = time.time()
    return finalTime - initTime

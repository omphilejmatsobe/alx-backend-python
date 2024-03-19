#!/usr/bin/env python3

"""
Couroutine call that takes in int arguments and returns list of
all the delays from wait_random
"""

from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns list of all the dlays from task_wait_random """

    delays: List[float] = []
    all_delays: List[float] = []

    for i in range(n):
        delays.append(task_wait_random(max_delay))

    for i in asyncio.as_completed(delays):
        _result = await i
        all_delays.append(_result)
    return all_delays

#!/usr/bin/env python3
'''Task 0: Async Generator
'''
import asyncio
import random
import typing


async def async_generator() -> typing.Iterator[int]:
    '''The coroutine will loop 10 times, each time asynchronously
    wait 1 second then yield a random number between 0 and 10.
    '''
    for i in range(10):
        yield random.random() * 10
        await asyncio.sleep(1)

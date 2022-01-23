"""script.py."""

import asyncio
import random
from hashlib import sha256


# async functions
async def name():
    """Name."""
    await asyncio.sleep(random.randint(0, 5))
    print('Дмитрий')


async def job():
    """Job."""
    await asyncio.sleep(random.randint(0, 5))
    print('Стажёр-программист Python / Python Developer Trainee')


async def money():
    """Money."""
    await asyncio.sleep(random.randint(0, 5))
    print('80000р')


async def asynchonous():
    """Acync."""
    tasks = [
        ioloop.create_task(name()),
        ioloop.create_task(money()),
        ioloop.create_task(job()),
    ]
    await asyncio.wait(tasks)


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchonous())
ioloop.close()


stdin = input()

print(sha256(stdin.encode('utf-8')).hexdigest())

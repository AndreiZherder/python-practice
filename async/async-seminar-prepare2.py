import asyncio
import random
import time


@asyncio.coroutine
def clock():
    while True:
        print(time.strftime('%H:%M:%S', time.localtime()))
        yield from asyncio.sleep(1)


@asyncio.coroutine
def message():
    for i in range(5):
        print('Bang')
        yield from asyncio.sleep(random.randrange(5))
    return 'DONE!'


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(clock())
    res = loop.run_until_complete(message())
    print(res)

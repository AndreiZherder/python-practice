import heapq
import time
import types


@types.coroutine
def sleep(delay):
    yield delay


async def rhythm():
    print('1')
    for i in range(10):
        await sleep(1)
        print('1')


async def bang():
    print('Bang')
    for i in range(5):
        await sleep(3)
        print('Bang')


def main():
    tasks = []
    heapq.heappush(tasks, (time.time(), 1, bang()))
    heapq.heappush(tasks, (time.time(), 2, rhythm()))
    while tasks:
        start_time, priority, task = heapq.heappop(tasks)
        wait = start_time - time.time()
        if wait > 0:
            time.sleep(wait)
        try:
            start_time = task.send(None) + time.time()
        except StopIteration:
            continue
        heapq.heappush(tasks, (start_time, priority, task))


if __name__ == '__main__':
    main()

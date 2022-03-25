import heapq
import time


def sleep(delay):
    yield delay


def rhythm():
    print('1')
    for i in range(10):
        yield from sleep(1)
        print('1')


def bang():
    print('Bang')
    for i in range(10):
        yield from sleep(3)
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
            start_time = next(task) + time.time()
        except StopIteration:
            continue
        heapq.heappush(tasks, (start_time, priority, task))


if __name__ == '__main__':
    main()

import heapq
import time


def sleep(delay):
    yield time.time() + delay


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
    task1 = bang()
    task2 = rhythm()
    tasks = []
    priority = {task1: 1, task2: 2}
    heapq.heappush(tasks, (time.time(), priority[task1], task1))
    heapq.heappush(tasks, (time.time(), priority[task2], task2))
    while tasks:
        start_time, _, task = heapq.heappop(tasks)
        wait = start_time - time.time()
        if wait > 0:
            time.sleep(wait)
        try:
            start_time = next(task)
        except StopIteration:
            pass
        else:
            heapq.heappush(tasks, (start_time, priority[task], task))


if __name__ == '__main__':
    main()

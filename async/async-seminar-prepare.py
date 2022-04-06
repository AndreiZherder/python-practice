import heapq
import random
import time


def sleep(delay):
    yield delay


def clock():
    while True:
        print(time.strftime('%H:%M:%S', time.localtime()))
        yield from sleep(1)


def message():
    while True:
        print('Bang')
        yield from sleep(random.randrange(5))


class Loop:
    def __init__(self):
        self.tasks = []
        self.task_id = 0

    def create_task(self, start_time, task):
        heapq.heappush(self.tasks, (start_time, self.task_id, task))
        self.task_id += 1

    def run(self):
        while self.tasks:
            start_time, task_id, task = heapq.heappop(self.tasks)
            wait = start_time - time.time()
            if wait > 0:
                time.sleep(wait)
            try:
                delay = next(task)
            except StopIteration:
                continue
            heapq.heappush(self.tasks, (time.time() + delay, task_id, task))


def main():
    loop = Loop()
    loop.create_task(time.time(), message())
    loop.create_task(time.time(), clock())
    loop.run()


if __name__ == '__main__':
    main()

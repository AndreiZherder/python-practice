from collections import deque


def rhythm():
    for i in range(10):
        yield
        print('1')


def bang():
    cnt = 0
    for i in range(10):
        yield
        if cnt % 3 == 0:
            print('Bang')
        cnt += 1


def main():
    task1 = bang()
    task2 = rhythm()
    tasks = deque([task1, task2])
    while tasks:
        task = tasks.popleft()
        try:
            next(task)
        except StopIteration:
            pass
        else:
            tasks.append(task)



if __name__ == '__main__':
    main()

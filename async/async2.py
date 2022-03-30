import asyncio


async def rhythm():
    print('1')
    for i in range(10):
        await asyncio.sleep(1)
        print('1')


async def bang():
    print('Bang')
    for i in range(5):
        await asyncio.sleep(3)
        print('Bang')


async def main():
    # task1 = asyncio.create_task(bang())
    # task2 = asyncio.create_task(rhythm())
    # await task1
    # await task2
    await asyncio.gather(bang(), rhythm())


if __name__ == '__main__':
    asyncio.run(main())

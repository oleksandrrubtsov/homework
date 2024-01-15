import asyncio

# Створіть 3 асинхронні функції: task1(), task2(), та task3(). Кожна з цих функцій повинна мати асинхронну затримку, наприклад, за допомогою asyncio.sleep().
# Створіть асинхронну функцію main(), яка викликає ці три функції.
# Запустіть цю основну функцію і спостерігайте порядок виконання задач.

# В коментарях до коду зазначте, в якому порядку викликаються асинхронні задачі.
# Спробуйте різні комбінації виклику функцій в main(), щоб побачити, як змінюється порядок виконання.
# Зверніть увагу на різницю між асинхронним та синхронним виконанням коду.

async def task1():
    await asyncio.sleep(4)
    print("Task 1 is completed")

async def task2():
    await asyncio.sleep(2)
    print('Task 2 is completed')

async def task3():
    await asyncio.sleep(9)
    print('Task 3 is completed')

async def main():
    task1_future = asyncio.create_task(task1())
    task2_future = asyncio.create_task(task2())
    task3_future = asyncio.create_task(task3())

    await task1_future
    await task2_future
    await task3_future

if __name__ == "__main__":
    asyncio.run(main())



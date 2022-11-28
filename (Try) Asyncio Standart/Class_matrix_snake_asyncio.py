import random
import asyncio

"""
C помощью библиотеки from typing import Optional и
указания в классе __init__(concurrent_level: Optional[int] = None)
Можно указать максимальное количество параллельных запросов
self.concurrent_level = concurrent_level , создание переменной запросов в __init__
self.НАЗВАНИЕ ФУНКЦИИ_task: Optional[Тип переменной] = None , обозначение функции
Для сохранения в память self.НАЗВАНИЕ ФУНКЦИИ_task = asyncio.create_task(self.НАЗВАНИЕ ФУНКЦИИ)
"""


class MatrixSnake:
    def __init__(self, n: int, n_min: int, n_max: int, interval: int = 1):
        self.n = n
        self.n_min = n_min
        self.n_max = n_max
        self.interval = interval
        self.is_running = False

    async def _matrix_edit_fun(self):
        matrix = list()
        while self.is_running:
            for _ in range(self.n):
                matrix.append([
                    int(random.randint(self.n_min, self.n_max))
                    for _ in range(self.n)])
            await asyncio.sleep(self.interval)
        return matrix

    def start(self):
        self.is_running = True
        asyncio.create_task(self._matrix_edit_fun())


async def start():
    matrix_snake = MatrixSnake(5, -10, 10)
    matrix_snake.start()
    await asyncio.sleep(5)


def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        loop.close()


if __name__ == '__main__':
    print(main())

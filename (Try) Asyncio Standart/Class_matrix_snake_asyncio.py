import random
import asyncio
from typing import Optional

"""
C помощью библиотеки from typing import Optional и
указания в классе __init__(concurrent_level: Optional[int] = None)
Можно указать максимальное количество параллельных запросов
self.concurrent_level = concurrent_level , создание переменной запросов в __init__
self.НАЗВАНИЕ ФУНКЦИИ_task: Optional[Тип переменной] = None , обозначение функции
Для сохранения в память self.НАЗВАНИЕ ФУНКЦИИ_task = asyncio.create_task(self.НАЗВАНИЕ ФУНКЦИИ)
"""


class MatrixSnake:
    def __init__(self, n: int, n_min: int, n_max: int, interval: int = 1, concurrent_level: Optional[int] = None):
        self.n = n
        self.n_min = n_min
        self.n_max = n_max
        self.interval = interval
        self.concurrent_level = concurrent_level
        self.is_running = False
        self._matrix_edit_task: Optional[asyncio.Task] = None

    async def _matrix_edit_fun(self):
        matrix = list()
        while self.is_running:
            for _ in range(self.n):
                matrix.append([
                    int(random.randint(self.n_min, self.n_max))
                    for _ in range(self.n)])
            await asyncio.sleep(self.interval)
        return matrix

    # async def _matrix_check_fun(self):
    #     matrix_check = asyncio.create_task(self._matrix_edit_fun())
    #     # Сравнение строк (длины списков) и столбцов (количество списков)
    #     while self.is_running:
    #         for list_check in matrix_check:
    #             if len(list_check) != len(matrix_check):
    #                 return self.is_running is False
    #         await asyncio.sleep(self.interval)
    #     return matrix_check

    def start(self):
        self.is_running = True
        self._matrix_edit_task = asyncio.create_task(self._matrix_edit_fun())


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

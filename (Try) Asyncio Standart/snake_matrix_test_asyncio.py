import matrix_snake_asyncio as ms
import asyncio


async def main():
    await ms.snake_matrix(5, -10, 10)


print(main())

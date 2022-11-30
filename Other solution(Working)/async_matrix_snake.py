import asyncio
import aiohttp
import logging
import re

logger = logging.getLogger(__name__)


async def get_page(session, url: str) -> (str | None):
    try:
        async with session.get(url) as r:
            return await r.text()

    except aiohttp.ClientConnectorError as ex:
        logger.error(f'Ошибка соединения: {ex}')

    except asyncio.TimeoutError as ex:
        logger.error(f'Запрос занимает слишком много времени: {ex}')


async def get_data(session, url):
    task = asyncio.create_task(get_page(session, url))
    results = await asyncio.gather(task)
    return results


async def main(url):
    async with aiohttp.ClientSession() as session:
        data = await get_data(session, url)
        return data


def matrix_check_fun(matrix: str) -> (list[list[int]] | bool):
    """
    Было бы интересно узнать как можно сделать не results[0], а в цикле for,
    то есть -> for result in results, так как он требует глобальных переменных,
    в своем проекте я использовал счетчики для переменных, то есть -> globals()["название" + str(i)]

    Находим все значения из списка только числа с помощью отборки в виде \d+
    """
    output = [re.findall(r'\d+', matrix[0])]
    output = output[0]
    """
    1. Нахожу квадратный корень из массива(то есть, то, сколько может быть в одной строке),
    для равномерного массива, нужны одинаковые числа то есть, как в нашем примере 4 на 4, все равно что,
    все наши элементы равны 16 - в квадратном корне равны 4
    """
    sqrt = int(len(output) ** 0.5)
    matrix_output = []
    while output:
        matrix_output.append(output[:sqrt])
        output = output[sqrt:]

    try:
        for list in matrix_output:
            if len(list) != len(matrix_output):
                return False

    except ValueError as ex:
        logger.warning(ex)
        return []

    return matrix_output


def matrix_sort_fun(matrix: list[list[int]], output: list[int] = None) -> list[int]:
    N = len(matrix)
    output = list()

    for j in range(N - 1, -1, -1):
        for i in matrix:
            output.append(i[j])

    return output


def matrix_format_fun(matrix_check: list[list[int]], matrix_sort: list[int], output: list[list[int]] = None) -> list[list[int]]:
    output = list()

    list_size = len([len(list_input) for list_input in matrix_check])

    for i in range(0, len(matrix_sort), list_size):
        output.append(matrix_sort[i:i + list_size])

    return output


async def get_matrix(SOURCE_URL: str) -> list[list[int]]:
    results = await main(SOURCE_URL)
    return matrix_format_fun(matrix_check_fun(results), matrix_sort_fun(matrix_check_fun(results)))

"""
if __name__ == "__main__":
    SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
    results = asyncio.run(main(SOURCE_URL))
    # print(matrix_format_fun(matrix_check_fun(results), matrix_sort_fun(matrix_check_fun(results))))
    print(matrix_format_fun(matrix_check_fun(results), matrix_sort_fun(matrix_check_fun(results))))
"""
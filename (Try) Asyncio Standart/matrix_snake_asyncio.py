import random
import asyncio


async def matrix_edit_fun(n: int, n_min: int, n_max: int) -> list:
    global matrix
    matrix = list()
    for _ in range(n):
        matrix.append([
            int(random.randint(n_min, n_max))
            for _ in range(n)])
    # Для понимания как работает сортировка ->
    # k = 0
    # for _ in range(n):
    #     matrix.append([
    #         int(k)
    #         for _ in range(n)
    #     ])
    #     k += 1
    # Для проверки работы ->
    # matrix.append(["aaa",10,10,10,10])
    return matrix


async def matrix_check_fun(n: int, n_min: int, n_max: int) -> list:
    matrix_check = await matrix_edit_fun(n, n_min, n_max)
    for matrix in matrix_check:
        # Сравнение строк (длины списков) и столбцов (количество списков)
        for list_check in matrix:
            if len(list_check) == len(matrix_check):
                return matrix_check


async def matrix_sort_fun(n: int, n_min: int, n_max: int) -> list:
    matrix_check_output = await matrix_check_fun(n, n_min, n_max)
    N = len(matrix_check_output)
    matrix_sort_output = list()

    """
    Помогите понять, я не знаю как это получилось
    
    В частности цикл ниже не работает если брать как элемент матрицы,
    то есть for i in range(N) - не работает, а
    for j in range(N-1,-1,-1) используется для поворота.
    """

    for j in range(N - 1, -1, -1):
        for i in matrix_check_output:
            matrix_sort_output.append(i[j])

    return matrix_sort_output


async def matrix_format_fun(n: int, n_min: int, n_max: int) -> list:
    matrix_check = await matrix_check_fun(n, n_min, n_max)
    matrix_form = await matrix_sort_fun(n, n_min, n_max)
    matrix_form_output = list()

    # Создаю функцию для нахождения размера списка,
    # в данном случае он проходит по всем и записывает последний только (его размер)

    list_size = len([len(list_input) for list_input in matrix_check])

    # Цикл выполняет разделение нашего списка из matrix_sort_fun(),
    # Выбирает начальный элемент 0, длина нашего выведенного списка сортировкой
    # И размер одного списка в виде шага
    # далее добавляются в новый массив элементы начиная с i до того же плюс размер списка
    # Например append(0:0+5) - первый массив

    for i in range(0, len(matrix_form), list_size):
        matrix_form_output.append(matrix_form[i:i + list_size])

    return matrix_form_output


async def snake_matrix(n, n_min, n_max):
    # matrix_form = await asyncio.matrix_format_fun(
    #     await asyncio.matrix_sort_fun(
    #         await asyncio.matrix_check_fun(
    #             await asyncio.matrix_edit_fun(n, n_min, n_max)
    #         )
    #     )
    # )
    matrix = asyncio.create_task(matrix_edit_fun(n, n_min, n_max))
    matrix_check = asyncio.create_task(matrix_check_fun(n, n_min, n_max))
    matrix_sort = asyncio.create_task(matrix_sort_fun(n, n_min, n_max))
    matrix_form = asyncio.create_task(matrix_format_fun(n, n_min, n_max))
    await matrix, matrix_check, matrix_sort, matrix_form
    return matrix_form

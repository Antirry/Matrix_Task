import random


def matrix_edit_fun(n, n_min, n_max):
    global matrix
    matrix = list()
    for _ in range(n):
        matrix.append([
            int(random.randint(n_min, n_max))
            for _ in range(n)
        ])
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


def matrix_check_fun(matrix_check):
    # Сравнение строк (длины списков) и столбцов (количество списков)
    for list_check in matrix_check:
        if len(list_check) != len(matrix_check):
            return False

    return matrix_check


def matrix_sort_fun(matrix_sort):
    N = len(matrix_sort)
    matrix_sort_output = list()

    """
    Помогите понять, я не знаю как это получилось
    
    В частности цикл ниже не работает если брать как элемент матрицы,
    то есть for i in range(N) - не работает, а
    for j in range(N-1,-1,-1) используется для поворота.
    """

    for j in range(N - 1, -1, -1):
        for i in matrix_sort:
            matrix_sort_output.append(i[j])

    return matrix_sort_output


def matrix_format_fun(matrix_form):
    matrix_check = matrix_check_fun(matrix)
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


def snake_matrix(n, n_min, n_max):
    return matrix_format_fun(matrix_sort_fun(matrix_check_fun(matrix_edit_fun(n, n_min, n_max))))

import random


def matrix_edit_fun(n):
    matrix = list()
    for _ in range(n):
        matrix.append([
            int(random.randint(1, 100))
            for _ in range(n)
        ])
    # matrix.append(["aaa",32321,321312,321312,3321312,321312])

    return matrix


def matrix_check_fun(matrix_check):
    # Сравнение строк (длины списков) и столбцов (количество списков)
    for list in matrix_check:
        if len(list) != len(matrix_check):
            return False

    return matrix_check


def matrix_sort_fun(matrix_sort):
    N = len(matrix_sort)
    for i in range(N):
        for j in range(N):
            matrix_sort[i][j] = 0
    return matrix_sort


if __name__ == '__main__':
    # Input_Matrix = int(input("Введите одним числом размер матрицы - "))

    # Matrix = matrix_edit_fun(Input_Matrix)
    Matrix = matrix_edit_fun(5)
    Matrix_Check = matrix_check_fun(Matrix)
    print(Matrix_Check)
    Matrix_Sort = matrix_sort_fun(Matrix_Check)
    print(Matrix_Sort)
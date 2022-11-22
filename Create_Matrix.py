import random
import numpy as np


max_number1 = int(input("Задайте максимальное значение - "))
n_col1 = int(input("Задайте значение колонок - "))
n_rows1 = int(input("Задайте значение столбцов - "))


def Matrix_Edit_fun(max_number, n_col, n_rows):
    matrix = np.random.randint(max_number, size=(n_col, n_rows))
    return matrix


def Main_Create():
    Matrix = Matrix_Edit_fun(max_number1, n_col1, n_rows1)
    # Matrix = str(Matrix)
    return Matrix

import Create_Matrix
import numpy as np


def Check_Int_fun(matrix_int):
    integer = isinstance(matrix_int, np.intc)
    print(integer)
    print("Проверка на числа = ")
    try:
        if integer is not True:
            print("Имеются не только числа")
            return -1
    except KeyError:
        print("Имеются только числа (", integer is True, ")")
        return matrix_int


def Check_Col_Row_fun(matrix_cols_rows):
    rows, columns = matrix_cols_rows.shape
    print("Проверка на колонки и строки = ")
    try:
        rows != columns is print("Не квадратичная")
    except KeyError:
        print("Квадратичная = ", rows, columns)
        return matrix_cols_rows


if __name__ == '__main__':
    Matrix = Create_Matrix.Main_Create()
    Matrix_check_int = Check_Int_fun(Matrix)
    if Matrix_check_int is True:
        Check_Col_Row = Check_Col_Row_fun(Matrix_check_int)

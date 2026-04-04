"""В матрице найти сумму и произведение элементов столбца N (N задать с
клавиатуры)"""
from functools import reduce
from random import randint

def get_mat(num):
    return [[randint(-5, 5) for i in range(randint(2, 7))] for i in range(num)]

num = int(input("Введите число столбов матрицы: "))
N = int(input("Введите натуральное число, что меньше числа столбцов: "))

def main():
    mat = get_mat(num)
    count = reduce(lambda x, y: x + y, mat[N])
    prod = reduce(lambda x, y: x * y, mat[N])
    print(mat[N])
    return count, prod

a, b = main()
print(f"Сумма элементов столбца равна {a}\nПроизведение элементов столбца равно {b}")

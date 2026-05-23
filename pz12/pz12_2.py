'''В матрице найти отрицательные элементы, сформировать из них новый массив.
Вывести размер полученного массива.'''
from random import  randint

string = int(input("Введите число строк внутри матрицы: "))
lens =  int(input("Введите максимальную длину строки: "))

mat = [[randint(-10, 10) for i in range(randint(1, lens))] for j in range(string)]

print(f"Матрица: {mat}")

mass = [i for j in mat for i in j if i < 0]

print(f"Единый массив: {sorted(mass)}")

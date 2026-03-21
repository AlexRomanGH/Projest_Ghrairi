'''1.Организовать и вывести последовательность из N случайных целых чисел. Из
исходной последовательности организовать новую последовательность, содержащую
положительные числа. Найти их количество.'''

from random import randint

def getl(n):
    yield from [randint(-25, 25) for i in range(n)]

def poz(listh):
    return len(list(filter(lambda x: x > 0, listh)))

n = int(input("Введите число: "))

lis = list(getl(n))
print(lis)
print(poz(lis))

#Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементовсписка вправо на K позиций (при этом A1 перейдет в AK+1, A2 — в AK+2, ..AN-K — вAN, а исходное значение K последних элементов будет потеряно). Первые Kэлементов #полученного списка положить равными 0.
import random
lis = []

def get_list(N):
  for i in range(N):
    lis.append(random.randint(1, 9))

def main():
 N = input("Введите размер списка: ")
 while type(N) != int:
  try:
    N = int(N)
  except TypeError:
    print("Ошибка значения. Введите число: ")
    N = input("Введите целое число: ")

 get_list(N)
 print(lis)
 k = input("На сколько позиций сдвинуть список?: ")
 while type(k) != int:
  try:
    k = int(k)
  except TypeError:
    print("Ошибка. Введите новое значение: ")
    k = input("Введите значение: ")
  
  return [0] * k + lis[:-k]


print(main())

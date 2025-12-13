#Дан список A размера N (N — нечетное число). Вывести его элементы с нечетными номерами в порядке убывания номеров: AN, AN-2, AN-4, ..., A1. Условный оператор не использовать.
import random
lis = []

def get_list(N):
  for i in range(N):
    lis.append(random.randint(1, 10))

def main():
 N = input("Введите размер списка: ")
 while type(N) != int:
  try:
    N = int(N)
  except TypeError:
    print("Ошибка значения. Введите число: ")
    N = input("Введите целое число: ")

  get_list(N)
  print(f"Исходный список: {lis}")

 return f"Отформатированный список: lis[-1::-2]"

print(main())

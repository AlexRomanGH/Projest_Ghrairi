#Дан список размера N. Найти два соседних элемента, сумма которых максимальна, и вывести эти элементы в порядке возрастания их индексов
import random
lis = []

def get_list(N):
  for i in range(N):
    num = random.randint(1, 1000)
    lis.append(num)
  return(lis)

def main():
  N = input("Введите размер списка: ")
  while type(N) != int:
    try:
      N = int(N)
    except TypeError:
      print("Ошибка значения. Введите число: ")
      N = input("Введите целое число: ")

  get_list(N)
  print(f"Список:\n{lis}")
  a = -1
  b = -1

  max_sum = -10000000000000000000000000000000000000000000000000000000000
  for i in range(1, N):
    sum = lis[i] + lis[i - 1]
    if sum > max_sum:
      max_sum = sum
      a = lis[i - 1]
      b = lis[i]

  print(f"Элементы максимальной суммы соседних элементов в списке: {a}, {b}")

main()

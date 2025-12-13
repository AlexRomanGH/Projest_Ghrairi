#Дана непустая строка S и целое число N (> 0). Вывести строку, содержащую символы строки S, между которыми вставлено по N символов «*» (звездочка)
def stars(word, starsi):
  lis = []
  for i in word:
    lis.append(i)
  star = "*" * starsi
  return (result := star.join(lis))


def main():
  s = input("Введите слово: ")

  N = input("Введите число звезд: ")
  while type(N) != int:
    try:
      N = int(N)
    except TypeError:
      print("Вы ввели неправильное значение. Попробуйте снова: ")
      N = input("Введите число звезд: ")
  print(stars(s, N))

main()

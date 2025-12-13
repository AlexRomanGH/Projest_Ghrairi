
'''Дана строка-предложение на русском языке. Вывести самое короткое слово в
предложении. Если таких слов несколько, то вывести последнее из них. Словом
считать набор символов, не содержащий пробелов, знаков препинания и
ограниченный пробелами, знаками препинания или началом/концом строки.'''

def find_min_word(wordl):
  for i in ".,!?:;-":
    wordl = wordl.replace(i, "")

    lis = wordl.split()

    mini = lis[0]
    min_len = len(lis[0])

    for i in lis:
      if len(i) <= min_len:
        min_len = len(i)
        mini = i
  return mini

def main():
  word = input("Введите текст: ")
  print(f"Самое короткое слово в предложении: {find_min_word(word)}")

main()

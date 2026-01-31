#2. Организовать словарь на 10 англо-русских слов, обеспечивающий "перевод" английского слова на русский.
biblio = {'Cat': 'Кошка', 'Dog': 'Собака', 'Sun': 'Солнце', 'Moon': 'Луна', 'Nation': 'Нация', 'War': 'Война', 'King': 'Король', 'Leader': 'Лидер', 'Money': 'Деньги', 'Terror': 'Ужас'}

dom = biblio.keys()

while True:
    click = input("Введите ключ")
    if click in dom:
        biblio.get(input())
    elif click == "0":
        print("Работа окончена")
        break
    else:
        print("Данного ключа нет в словаре")

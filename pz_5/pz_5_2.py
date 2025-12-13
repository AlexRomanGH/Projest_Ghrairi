'''Описать функцию SortDec3(A, B, C), меняющую содержимое переменных A, B, C
таким образом, чтобы их значения оказались упорядоченными по убыванию (A, B,
C — вещественные параметры, являющиеся одновременно входными и
выходными). С помощью этой функции упорядочить по убыванию два данных'''
набора из трех чисел: (A1, B1, C1) и (A2, B2, C2).
def replaces(a, b, c):
    if a > b and a > c:
        if c > b:
            return b, c, a
        else:
            return c, b, a
    elif b > a and b > c:
        if a > c:
            return c, a, b
        else:
            return a, c, b
    else:
        if a > b:
            return b, a, c
        else:
            return a, b, c
           
a1 = input("Введите число")

while type(a1) != int:
    try:
        a1 = int(a1)
    except ValueError:
        print("Ошибка данных, попробуйте еще раз")
        a1 = input("Введите число: ")
       
b1 = input("Введите число")

while type(b1) != int:
    try:
        b1 = int(b1)
    except ValueError:
        print("Ошибка данных, попробуйте еще раз")
        b1 = input("Введите число: ")

c1 = input("Введите число")

while type(c1) != int:
    try:
        c1 = int(c1)
    except ValueError:
        print("Ошибка данных, попробуйте еще раз")
        c1 = input("Введите число: ")
       
a2 = input("Введите число")

while type(a2) != int:
    try:
        a2 = int(a2)
    except ValueError:
        print("Ошибка данных, попробуйте еще раз")
        a2 = input("Введите число: ")
       
b2 = input("Введите число")

while type(b2) != int:
    try:
        b2 = int(b2)
    except ValueError:
        print("Ошибка данных, попробуйте еще раз")
        b2 = input("Введите число: ")

c2 = input("Введите число")

while type(c2) != int:
    try:
        c2 = int(c2)
    except ValueError:
        print("Ошибка данных, попробуйте еще раз")
        c2 = input("Введите число: ")

a1, b1, c1 = replaces(a1, b1, c1)
a2, b2, c2 = replaces(a2, b2, c2)

print(a1, b1, c1)
print(a2, b2, c2)

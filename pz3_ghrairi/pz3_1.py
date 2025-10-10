# Даны три целых числа: A, B, C. Проверить истинность высказывания: «Каждое из чисел A, B, C положительное».


a, b, c = input('Введите целое число: '), input('Введите целое число: '), input('Введите целое число: ')

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно. Введите число")
        a = input('Введите целое число: ')

while type(b) != int:
    try:
        b = int(a)
    except ValueError:
        print("Неправильно. Введите число")
        b = input('Введите целое число: ')

while type(c) != int:
     try:
        c = int(c)
     except ValueError:
        print("Неправильно. Введите число")
        c = input('Введите целое число: ')

if a > 0 and b > 0 and c > 0:
    print("Истина, все числа положительны")
else:
    print("Ложь,  все или некоторые числа отрицательны или равны нулю")

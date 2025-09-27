#Дано двузначное число. Найти сумму и произведение его цифр.

try:
    num = int(input("Введите двузначное число: "))
except ValueError:
    print("Это не число")
    
try:
    summa = num // 10 + num % 10
    proz = num // 10 * num % 10

    print(f"Сумма цифр: {summa}\nПроизведение чисел: {proz}")
except NameError:
    print("Нет данных")

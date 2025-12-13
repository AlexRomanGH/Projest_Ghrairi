def summator(n):
    count = 1
    summa = 0
   
    while count <= n:
        summa += count
        count += 1
       
    return summa

num = input("Введите число")

while type(num) != int:
    try:
        num = int(num)
    except ValueError:
        print("Ошибка данных, попробуйте еще раз")
        print("Введите число: ")
       
print(summator(num))

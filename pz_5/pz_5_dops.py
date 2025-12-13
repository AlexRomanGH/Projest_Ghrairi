#доп_1
#Даны три целых числа. Определить у какого числа больше сумма цифр. Вывод результата предусмотреть в основной программе. Расчет суммы цифр оформить в функции.   
num1 = int(input())
num2 = int(input())
num3 = int(input())

  
def print_max_sum(a, b, c):
    sum1 = 0
    sum2 = 0
    sum3 = 0
   
    while a != 0:
        sum1 += a % 10
        a //= 10
   
    while b != 0:
        sum2 += b % 10
        b //= 10
       
    while c != 0:
        sum2 += b % 10
        c //= 10
       
    if sum1 > sum2 and sum1 > sum3:
        return f"Наибольшей является сумма числа {num1} она равна {sum1}"
    elif sum2 > sum1 and sum2 > sum3:
        return f"Наибольшей является сумма числа {num2} она равна {sum2}"
    else:
        return f"Наибольшей является сумма числа {num3} она равна {sum3}"
   
print(print_max_sum(num1, num2, num3))

#доп_2
#Рассчитать и вывести периметр и площадь прямоугольника. Расчеты оформить в функции.  
num1 = int(input())
num2 = int(input())
num3 = int(input())

def triog(a, b, c):
    pert = a + b + c
    p = pert / 2
    plod = pow((p * (p - a) * (p - b) * (p - c)), 0.5)
    return f"Периметр треуголька {pert}, площадь треуголька {plod}"

print(triog(num1, num2, num3))

#доп_3
#Написать программу, подсчитывающую количество цифр числа, используя для этого функцию.   
num1 = int(input())

def num_count(num):
    count = 0
   
    while num != 0:
        count += 1
        num //= 10
   
    return f"В числе  {num1}  количество цифр равно {count}"

print(num_count(num1)) 

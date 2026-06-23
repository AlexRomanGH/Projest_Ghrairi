"""1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Исходные данные:
Количество элементов:
Максимальный элемент:
Среднее арифметическое элементов первой трети:"""

import random


sequence = [random.randint(-100, 100) for _ in range(12)]

with open("numbers.txt", "w") as f:
    for num in sequence:
        f.write(str(num) + "\n")

n = len(sequence)
max_elem = max(sequence)
first_third_count = n // 3
if first_third_count > 0:
    avg_first_third = sum(sequence[:first_third_count]) / first_third_count
else:
    avg_first_third = 0.0

with open("result_numbers.txt", "w") as f:
    f.write("Исходные данные:\n")
    for num in sequence:
        f.write(str(num) + "\n")
    f.write(f"Количество элементов: {n}\n")
    f.write(f"Максимальный элемент: {max_elem}\n")
    f.write(f"Среднее арифметическое элементов первой трети: {avg_first_third}\n")

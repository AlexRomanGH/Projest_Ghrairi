"""В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и
ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
текстовый файл все даты февраля в формате ДД/ММ/ГГГГ."""


import re

data = open("/home/student/Документы/dates.txt", "rt")


dat = re.compile(r'[0-3][0-9]\.[0-1][0-9]\.[0-9]+')

data = "\n".join([i.replace('\n', "") for i in data])

print(f"Даты в формате ДД/ММ/ГОД: {(on := re.findall(dat, data))}, число: {len(on)}")

dat = re.compile(r'[0-3][0-9]/[0-1][0-9]/[0-9]+')

print(f"Даты в формате ДД/ММ/ГГГГ:{(ti := re.findall(dat, data))}, число: {len(ti)}")

res = ti + on + re.findall(r'[0-1][0-9][.][0-3][0-9][.][0-9]+', data) + re.findall(r'[0-1][0-9]/[0-3][0-9]/[0-9]+', data)

print(f"Все даты: {len(list(set(res)))}")

del on
del ti

resx = open("/home/student/PycharmProjects/pythonProject7/febral.txt", "wt")

resx.write("\n".join(re.findall(r'[0-2][0-9]/02/[0-9]+', data)))
resx.close()

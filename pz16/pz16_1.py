"""Создайте класс "Животное" с атрибутами "имя" и "вид". Напишите метод, который
выводит информацию о животном в формате "Имя: имя, Вид: вид"""

class Animal:
    def __init__(self, name, race):
        self.race = race
        self.name = name

    def describe_animal(self):
        return f"Имя животного: {self.name}\nНазвание вида: {self.race}"

alive = Animal(input(), input())

print(alive.describe_animal())

"""Создайте базовый класс "Транспорт" со свойствами "марка", "модель" и "год
выпуска". От этого класса унаследуйте класс "Автомобиль" и добавьте в него
свойство "тип кузова". """

class Transport:
    def __init__(self, mark, model, year):
        self.mark = str(mark)
        self.model = str(model)
        self.year = str(year)

class Car(Transport):
    def __init__(self, mark, model, year, kuzov):
        super().__init__(mark, model, year)
        self.kuzov = str(kuzov)

MyCar = Car("BMV", "A12", 12, "Small")

print(MyCar.kuzov, MyCar.model, MyCar.year, MyCar.mark, sep="\n")

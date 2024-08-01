# Домашняя работа по уроку "Специальные методы классов"
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):       # осталось из прошлого задания. Здесь не вызывается
        for i in range(1, new_floor + 1):
            if 1 <= new_floor <= self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Памир', 4)
h1.__str__()
h2.__str__()
print(len(h1))
print(len(h2))
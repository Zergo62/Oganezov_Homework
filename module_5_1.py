# Домашняя работа по уроку "Атрибуты и методы объекта."
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if 1 <= new_floor <= self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break

h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Памир', 4)
h1.go_to(5)
print('')
h2.go_to(5)
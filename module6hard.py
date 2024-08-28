# Дополнительное практическое задание по модулю: "Наследование классов."
from math import pi
class Figure():
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = sides
        self.__sides = []
        self.set_sides(*sides)
        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 < r < 255 and 0 < g < 255 and 0 < b < 255:
            return r, g, b
        else:
            return self.__color

    def set_color(self, r, g, b):
        new_color = self.__is_valid_color(r, g, b)
        self.__color = list(new_color)
        return self.__color

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for i in sides:
                if i > 0 and isinstance(i, int):
                    continue
                else:
                    return False
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]
        elif len(new_sides) == 1 and self.sides_count == 12 and new_sides[0] > 0:
            self.__sides = []
            for i in range(12):
                self.__sides.append(*new_sides)
        elif self.__sides != []:
            pass
        else:
            self.__sides = []
            for i in range(self.sides_count):
                self.__sides.append(1)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        circle_square = (self.__radius ** 2) * pi
        return circle_square

class Triangle(Figure):
    def __init__(self):
        self.sides_count = 3

    def get_square(self):
        triangle_square = (self.__height * self.sides[0]) / 2
        return triangle_square

class Cube(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 12
        super().__init__(color, *sides)

    def get_volume(self):
        cube_volume = self._Figure__sides[0] ** 3
        return cube_volume

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
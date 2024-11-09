# Домашнее задание по теме "Потоки на классах"
import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def timer(self, name, power):
        self.counter = 0
        enemies = 100
        while enemies > 0:
            time.sleep(1)
            self.counter += 1
            enemies -= power
            print(f'{name} сражается {self.counter} день(дня)..., осталось {enemies} воинов')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.timer(self.name, self.power)
        print(f'{self.name} одержал победу спустя {self.counter} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
first_knight.start()
second_knight = Knight("Sir Galahad", 20)
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')
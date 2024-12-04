# Домашнее задание по теме "Логирование"
import logging
import unittest

# Начало кода из условия (скачан с Git)
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2
    def walk(self):
        self.distance += self.speed
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)
    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers
# Конец кода из условия

class RunnerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='utf-8',
                            format='%(asctime)s | %(levelname)s | %(message)s')

    def test_walk(self):
        try:
            r1 = Runner('Name', -10)
            for i in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50)
        except ValueError:
            logging.error('Ошибка', exc_info=True)
            logging.warning('Неверная скорость для Runner')
        logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            r2 = Runner(19, 15)
            for i in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100)
        except TypeError:
            logging.error('Ошибка', exc_info=True)
            logging.warning('Неверный тип данных для объекта Runner')
        logging.info('"test_run" выполнен успешно')

if __name__ == "__main__":
    unittest.main()
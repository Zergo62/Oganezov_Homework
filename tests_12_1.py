# Домашнее задание по теме "Простые Юнит-Тесты"
import runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        r1 = runner.Runner('Вини Пух')
        for _ in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    def test_run(self):
        r2 = runner.Runner('Пятачёк')
        for _ in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    def test_challenge(self):
        r3 = runner.Runner('Ослик Иа')
        r4 = runner.Runner('Сова')
        for _ in range(10):
            r3.run()
            r4.walk()
        self.assertNotEqual(r3.distance, r4.distance)

if __name__ == '__main__':
    unittest.main
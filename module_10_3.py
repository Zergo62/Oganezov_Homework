# Домашнее задание по теме "Блокировки и обработка ошибок"
import threading
import time
import random

class Bank(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.balance = 700
        self.lock = threading.Lock()
    def deposit(self):
        for i in range(100):
            random_int = random.randint(50, 500)
            with self.lock:
                if self.balance >= 500 and self.lock.locked():
                    self.balance += random_int
                    print(f'Пополнение: {random_int}. Баланс: {self.balance}')
            time.sleep(0.001)
    def take(self):
        for i in range(100):
            random_int = random.randint(50, 500)
            print(f'Запрос на {random_int}')
            with self.lock:
                if random_int <= self.balance:
                    self.balance -= random_int
                    print(f'Снятие: {random_int}. Баланс: {self.balance}')
                else:
                    print(f'Запрос отклонён, недостаточно средств')

            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
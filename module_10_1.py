# Домашнее задание по теме "Введение в потоки".
import threading
import time

def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(word_count):
        time.sleep(0.1)
        file.write(f'Какое-то слово № {i+1}\n')
    file.close()
    print(f'Завершилась запись в файл {file_name}')

start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish_time = time.time()
print(f'Работа потоков: {finish_time - start_time}')

start_time = time.time()
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(10, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(10, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(10, 'example8.txt'))
thread1.start()
thread1.join()
thread2.start()
thread2.join()
thread3.start()
thread3.join()
thread4.start()
thread4.join()
finish_time = time.time()
print(f'Работа потоков: {finish_time - start_time}')
# Домашнее задание по теме "Многопроцессное программирование"
import multiprocessing
import time

filenames = [f'./file {number}.txt' for number in range(1, 5)]
def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        all_data.append(line)

# линейный вызов
start_time = time.time()
read_info('file 1.txt')
read_info('file 2.txt')
read_info('file 3.txt')
read_info('file 4.txt')
finish_time = time.time()
print(f'{finish_time - start_time} (линейный)')

# мультипроцессорный вызов
# if __name__ == '__main__':
#     start_time = time.time()
#     with multiprocessing.Pool(processes=len(filenames)) as pool:
#         pool.map(read_info, filenames)
#     finish_time = time.time()
#     print(f'{finish_time - start_time} (многопроцессный)')
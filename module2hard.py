import random
print('Дополнительное практическое задание по модулю: "Основные операторы"')
numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = random.choice(numbers)
print(f'Random number: {n}')
result = []
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if n % (i + j) == 0:
            result.append(i)
            result.append(j)

# print(f'Result: {result}')
print('Result: ', *result, sep='')



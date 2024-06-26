print('Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."')
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and first == third:
    print(3, '"Все три числа равны!"')
elif first == second or first == third or second == third:
    print(2, '"Равны два числа из трех!"')
else:
    print(0, '"Равных чисел нет!"')
print('Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"')
immutable_var = 15, 36, 'собака', 'кошка'
print('immutable_var:', immutable_var)
# immutable_var[1] = 'попугай'
# строка 4 не может быть исполнена, т.к. элементы кортежа не подлежат изменению
mutable_list = ['яблоко', 'банан', 'груша', 'персик']
mutable_list.append('манго')
mutable_list.remove('груша')
print('mutable_list:', mutable_list)
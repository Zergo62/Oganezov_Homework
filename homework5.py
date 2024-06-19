print('Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"')
immutable_var = 15, 36, 'собака', 'кошка'
print('immutable_var:', immutable_var)
mutable_list = ['яблоко', 'банан', 'груша', 'персик']
mutable_list.append('манго')
mutable_list.remove('груша')
print('mutable_list:', mutable_list)
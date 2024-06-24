print('Практическое задание по теме: "Словари и множества"')
my_dict = {'Sergo': 1983, 'Denis': 1981, 'Bob': 1972}
print('Dict:', my_dict)
print('Existing value:', my_dict['Sergo'])
print('Not existing value:', my_dict.get('Ivan'))
my_dict.update({'Petr': 1971,
                'Alex': 1969})
a = my_dict.pop('Bob')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
print(' ')

my_set = {'Ivan', 1, 3, 5.6, 1, 3, 4, (34, 48, 61)}
print('Set:', my_set)
my_set.add('Vadim')
my_set.add(2)
my_set.remove(1)
print('Modified set:', my_set)
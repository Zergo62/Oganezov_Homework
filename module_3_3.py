# Самостоятельная работа по уроку "Распаковка позиционных параметров".
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print('')

values_list = [66, 3.14, 'Test']
values_dict = {"a": 55, 'b': 1.25, 'c': 'Test2'}
print_params(*values_list)
print_params(**values_dict)
print('')

values_list_2 = [99, 'Строка']
print_params(*values_list_2, 42)
